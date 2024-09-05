# vdf_parser

Converts [vdf files](https://developer.valvesoftware.com/wiki/KeyValues) to dicts and back. Based on [JS Library vdf-parser](https://github.com/p0358/vdf-parser). 


### Functions
```
parseVdf(text):
Converts a text representation of vdf file into a dictionary
    :param text: (str) vdf text
    :returns: (dict) representation of vdf file
```
```
dump(vdf,indentLevel=0):
Converts dictionary back to vdf
    :param vdf: Parsed vdf dict
    :param indentLevel: Level of indentation
    :return: A string representation of vdf file
```



Options are set when instantiating
```
options= {
  "types":True/False, #attempt to convert values to data types default True
  "arrayify": True/False, #create lists out of repeated keys to retain them default True
  "conditionals":[] #conditionals to consider [$DEBUG] [!DEBUG] etc default None 
}
```


### Usage
```
vdf = VDF(options)
parsed = vdf.parseVdf(vdfString)
vdfString = vdf.dump(parsed)
```
