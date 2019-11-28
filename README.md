# Simplified-Traditional Chinese converter
A very simple python script to convert text files between simplified Chinese and traditional Chinese.

簡單的Python程序，可以將中文繁體和簡體互相切換。

简单的Python程序，可以将中文繁体和简体互相切换。

I made this primarily to convert .srt files, but should work with text files in general. 
Based on [this tutorial](https://yarnthen.github.io/yarnthencohosking/how%20to/2019/03/31/python-convert-traditional-simplified.html),
with some additional features and code changes.

## Usage
`python converter.py -i <inputfile> -o <outputfile> -l <input character type>`

Valid options for `-l` are `s` or `t`. This option specifies whether the input file is in **s**implified or **t**raditional characters. Defaults to simplified.

If the output file already exists, the script will overwrite it.


