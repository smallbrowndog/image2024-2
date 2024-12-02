from retinaface import RetinaFace

resp = RetinaFace.detect_faces('./img/children.jpg')
print(resp)