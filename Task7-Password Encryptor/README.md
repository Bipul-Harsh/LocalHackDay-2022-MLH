<div align="center">

# Noob Encrypter
Encrypt and decrypt password with noob logic :smile:

</div>

## To Encryption

### With Default Key

```bash
python3 main.py --encrypt "<password>"
```

### With Custom Key

```bash
python3 main.py --encrypt "<password>" --key <key>
```

## To Decrypt

```bash
python3 main.py --decrypt "<password>"
```

## Getting Help

```bash
python3 main.py --help
```

## Output

### Encryption
```bash
python3 main.py --encrypt "hello bello"
Encrypted password: yvvol*yvvor
Key: 0
```

### Decryption
```bash
python3 main.py --decrypt "yvvol*yvvor"
Decrypted password: hello bello
```