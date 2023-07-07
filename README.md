# SG and TRK Conversion Tools

This project provides Python scripts for converting SG files to TRK files readable by Papyrus IndyCar Racing 2, along with additional tools to convert SG and TRK files to CSV files, and TRK files to TXT format.

## Scripts

### SG to CSV Converter

- `sg2csv.py`: Converts an SG file into two CSV files, corresponding to header/xsects and section info.
- `csv2sg.py`: Reverses the operation carried out by `sg2csv.py`, converting the two CSV files back into an SG file.

#### Usage

To create CSV files from an SG file:

```bash
python sg2csv.py track.sg
```

To convert CSV files back to an SG file:

```bash
python csv2sg.py track.sg_header_xsects.csv track.sg_sects.csv track.sg
```

### SG to TRK Converter

- `sg2trk.py`: Converts an SG file to a TRK file. It also provides options to export the resulting TRK data into a CSV or TXT file.

#### Usage

To convert an SG file to a TRK file:

```bash
python sg2trk.py [track].sg
```

By default, this will create a file called `[track].trk`.

Options:

- `-f [csv, txt]`: Specifies the output format for the TRK data. Can be either `csv` for a series of CSV files or `txt` for a single TXT file.
- `-o [filename]`: Specifies the output filename. If not provided, the output file will have the same name as the input SG file.

### Supporting Modules

- `sg_classes.py`: Provides the `SGFile` class, which represents an SG file.
- `trk_classes.py`: Provides the `TRKFile` class, which represents a TRK file.
- `utils.py`: Contains utility methods used by the SG to TRK converter.
- `trk_exporter.py`: Contains methods for exporting a `TRKFile` object to either CSV, TXT or TRK format.
