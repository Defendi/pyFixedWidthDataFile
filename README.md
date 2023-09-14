# Fixed Width Data File Creator
This is a simple library for creating fixed-width text data files or text files (txt or csv) separated by a certain separator character. 

You can use it to exchange data between APIS and other applications.


## Installation

To install the package, just run the command below:

`pip install pyFixedWidthDataFile`

## Usage

1) **Instantiate the class**:

`from pyFixedWidthDataFile import FWDataFile
app = FWDataFile(path_to_specs_folder, optional_separator)`


* path_to_specs_folder: Path to the folder containing the **Specs Files**;
* optional_separator: Separation character between fields (optional)

2) **Specs Files**: Files, JSON standard, with specifications of the fields contained in the lines (records).

Example: Header record for a fixed-width file of 40 columns
`{
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
}`

Open the record with "{", enter the name clause, it is mandatory. Open the list of objects of type field with "fields {", enter the id of the field and enter the characteristics of the field.

# Characteristics List
* name: (required) name of the field
* start_pos: (required) starting position
* end_pos: (required) end position
* format: (required) field type, which can be:
> 1. alpha: alphanumeric, text
> 2. num: numeric (integer, floating point)
* default: (optional) default value of the field, if there is no default value the field will not be filled with spaces, even if it is numeric.
* decimals: (optional) only for numeric fields, number of decimal places
* ignore: (optional) field to be ignored
* required: (optional) mandatory field
* regex: (optional) regular expression operations field

3) Inject the lines from the file::

`app.append_line("header",cod_client="1234",name_client="Alexandre Defendi")
`

4) use the result: 

`print(app)
`

"R000001PED1234 Alexandre Defendi       X"


## License

This project is under the MIT license. See the [LICENSE](LICENSE.txt) file for more details.
