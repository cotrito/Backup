var = input("nombre archivo : ").lower().strip()
posicion = var.rfind(".") +1
ext = var[posicion:]
match ext:
    case "png" | "gif":
        print("image/" + ext)
    case "jpg" | "jpeg" :
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/" + ext)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")


