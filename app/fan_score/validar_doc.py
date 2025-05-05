# app/fan_score/validar_doc.py
import face_recognition_models
import face_recognition
from pathlib import Path
from typing import Optional
from PIL import Image
import numpy as np

def carregar_imagem(caminho_arquivo: Path) -> Optional[np.ndarray]:
    """
    Carrega uma imagem e retorna um array numpy.
    Converte PDF em imagem se necessário (requer pdf2image).
    """
    if not caminho_arquivo.exists():
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return None

    if caminho_arquivo.suffix.lower() == ".pdf":
        try:
            from pdf2image import convert_from_path
            imagens = convert_from_path(str(caminho_arquivo))
            if imagens:
                print(f"PDF convertido com sucesso: {caminho_arquivo}")
                return np.array(imagens[0])
        except Exception as e:
            print(f"Erro ao converter PDF {caminho_arquivo}: {e}")
            return None
    else:
        try:
            imagem = face_recognition.load_image_file(str(caminho_arquivo))
            print(f"Imagem carregada com sucesso: {caminho_arquivo}")
            return imagem
        except Exception as e:
            print(f"Erro ao carregar imagem {caminho_arquivo}: {e}")
            return None

def verificar_identidade(pasta_usuario: Path) -> bool:
    """
    Compara o rosto da selfie com o rosto presente na imagem da frente do documento.
    Retorna True se os rostos forem compatíveis.
    """
    caminho_doc_frente = next(pasta_usuario.glob("documento_frente.*"), None)
    caminho_selfie = next(pasta_usuario.glob("selfie.*"), None)

    # Log: Verificando os caminhos dos arquivos
    print(f"Caminho documento frente: {caminho_doc_frente}")
    print(f"Caminho selfie: {caminho_selfie}")

    if not caminho_doc_frente or not caminho_selfie:
        print("Arquivos necessários não encontrados.")
        return False

    imagem_doc = carregar_imagem(caminho_doc_frente)
    imagem_selfie = carregar_imagem(caminho_selfie)

    if imagem_doc is None or imagem_selfie is None:
        print("Erro ao carregar as imagens.")
        return False

    # Obter os codificadores faciais
    rostos_doc = face_recognition.face_encodings(imagem_doc)
    rostos_selfie = face_recognition.face_encodings(imagem_selfie)

    if not rostos_doc:
        print("Nenhum rosto detectado no documento.")
    if not rostos_selfie:
        print("Nenhum rosto detectado na selfie.")

    if not rostos_doc or not rostos_selfie:
        print("Nenhum rosto detectado em uma das imagens.")
        return False

    # Compara o primeiro rosto detectado em cada imagem
    resultado = face_recognition.compare_faces([rostos_doc[0]], rostos_selfie[0])
    return resultado[0]
