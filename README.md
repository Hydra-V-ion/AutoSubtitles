# AutoSubtitles 🎬

Un utilitaire en ligne de commande développé en Python pour générer et incruster automatiquement des sous-titres dynamiques sur une vidéo. Conçu pour accélérer le montage de VODs et de clips, ce script combine la précision de reconnaissance vocale d'OpenAI Whisper avec la puissance de traitement vidéo de FFmpeg.

**Fonctionnalités Principales**
*   **Transcription temporelle fine :** Analyse audio et horodatage générés mot par mot.
*   **Affichage dynamique (Format Court) :** Regroupement intelligent du texte par blocs avec une limite stricte fixée à 10 caractères pour un rythme soutenu.
*   **Correction typographique :** Gestion algorithmique des apostrophes françaises pour éviter les coupures disgracieuses (ex: "c'est").
*   **Rendu haute qualité :** Incrustation directe des sous-titres via FFmpeg avec un encodage H.264 et un paramètre CRF de 18 pour garantir une qualité visuelle sans perte.

**Prérequis Système**
*   Python 3.8 ou supérieur.
*   **FFmpeg** installé sur le système (`sudo pacman -S ffmpeg` sous EndeavourOS, ou `sudo apt install ffmpeg` sous Debian/WSL).

**Installation**
1.  Cloner le dépôt et naviguer dans le dossier du projet.
2.  Créer et activer un environnement virtuel local :
    ```bash
    python3 -m venv venv_whisper
    source venv_whisper/bin/activate
    ```
3.  Installer la bibliothèque d'Intelligence Artificielle :
    ```bash
    pip install -U openai-whisper
    ```
    *(Note : Pour des performances optimales, il est recommandé d'installer au préalable PyTorch avec le support CUDA si la machine dispose d'un GPU Nvidia).*

**Utilisation**
L'exécution du script requiert le passage de trois arguments obligatoires dans le terminal :

```bash
python3 main_2.py <video_source> <video_sortie> <modele_whisper>
