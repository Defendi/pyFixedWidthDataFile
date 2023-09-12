# FWDataFile Creator
This is a simple library for creating fixed-width text data files or text files (txt or csv) separated by a certain separator character. 

You can use it to exchange data between APIS and other applications.


## Installation

To install the package, just run the command below:

<pre><code>pip install pyFixedWidthDataFile</code></pre>

## Usage

1) <b>Instantiate the class</b>:

<code>
from pyFixedWidthDataFile import FWDataFile

app = FWDataFile(path_to_specs_folder, optional_separator)
</code>

* path_to_specs_folder: Path to the folder containing the <b>Specs Files</b>
* optional_separator: Separation character between fields (optional)

2) <b>Specs Files</b>: Files, JSON standard, with specifications of the fields contained in the lines (records).

Example:
Header record for a fixed-width file of 40 columns

<pre><code>

{
	"name": "header",
	"fields": {
		"field_01": {
			"name": "register_type",
			"start_pos": 1,
			"end_pos": 3,
			"format": "alfa",
			"default": "R00"
		},
		"field_02": {
			"name": "batch_number",
			"start_pos": 4,
			"end_pos": 7,
			"format": "num",
			"default": 1
		},			
		"field_03": {
			"name": "type_reg",
			"start_pos": 8,
			"end_pos": 10
			"format": "alfa",
			"default": "PED"
		},
		"field_04": {
			"name": "cod_client",
			"start_pos": 9,
			"end_pos": 15,
			"format": "alfa"
		},
		"field_05": {
			"name": "name_client",
			"start_pos": 16,
			"end_pos": 39,
			"format": "alfa"
		},
		"field_06": {
			"name": "end_reg",
			"start_pos": 40,
			"end_pos": 40,
			"format": "alfa",
			"default": "X"
		}
    }
}

</code></pre>

Open the record with "{", enter the name clause, it is mandatory. Open the list of objects of type field with "fields {", enter the <b>id</b> of the field and enter the characteristics of the field:
# Characteristics List
* <b>name</b>: (required) name of the field
* <b>start_pos</b>: (required) starting position
* <b>end_pos</b>: (required) end position
* <b>format</b>: (required) field type, which can be:
> 1. alpha: alphanumeric, text
> 2. num: numeric (integer, floating point)
* <b>default</b>: (optional) default value of the field, if there is no default value the field will not be filled with spaces, even if it is numeric.
* <b>decimals</b>: (optional) only for numeric fields, number of decimal places
* <b>ignore</b>: (optional) field to be ignored
* <b>required</b>: (optional) mandatory field
* <b>regex</b>: (optional) regular expression operations field

3) <b>Inject the lines from the file:</b>:
<code>

app.append_line("header",cod_client="1234",name_client="Alexandre Defendi")

</code>

4) <b>use the result</b>: 


<code>
print(app)
</code>

"R000001PED1234 Alexandre Defendi       X"


## License

This project is under the MIT license. See the [LICENSE](LICENSE.txt) file for more details.
