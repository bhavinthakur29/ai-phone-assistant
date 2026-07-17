from axion.nexus import ADBTransport


adb = ADBTransport()

result = adb.execute(
    ["devices"]
)

result.raise_for_error()

print(result.stdout)
print(result.success)