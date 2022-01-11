<div align="center">

# Image Pixelator
Pixelate any given image as argument.

</div>

## Instructions for use

- [Installing Requirements](#installing-requirements)
- [Runing Script](#runing-script)

### Installing Requirements

#### Windows

```bash
pip3 install -r requirements.txt
```
#### Linux

```bash
pip3 install -r requirements.txt
```

### Running Script

#### Help Command

```bash
python3 main.py -h
```

#### Running Default Image in Default Settings

```bash
python3 main.py
```

#### Running Custom Image

```bash
python3 main.py --input_file <file path>
```

#### Providing Custom Blur Value

Keep it below 1 and above 0.
```bash
python3 main.py --blur 0.05
```

## Output
![output1](assets/outputs/output.png)