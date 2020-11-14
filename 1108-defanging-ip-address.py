def defang_ip(ip:str) -> str:
  defanged = ""
  for i in ip:
    if i == ".":
      defanged += "[.]"
    else:
      defanged += i
    
  return defanged


def main():
  ip = "192.168.1.1"
  print(defang_ip(ip))


if __name__ == "__main__":
  main()
