import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'huehue-brbr'
  ALLOWED_EXTENSIONS = set(['txt', 'png', 'mov', 'mp3', 'mp4', 'webm', 'pdf', 'jpg', 'jpeg'])
  UPLOAD_FOLDER = os.path.join('app', 'uploads')
