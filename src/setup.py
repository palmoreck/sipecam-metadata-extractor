from setuptools import setup, find_packages

cli_list = "list_of_files_and_subdirectories_to_extract_metadata = simex.list_of_files_and_subdirectories_to_extract_metadata:main"
cli_extract_sn_coord = "extract_serial_number_and_coordinates_of_file = simex.extract_serial_number_and_coordinates_of_file:main"
cli_extract_met_and_ing = "extract_metadata_and_ingest_it = simex.extract_metadata_and_ingest_it:main"

setup(name="simex", version=0.1,
      description=u"Simplify extraction of metadata for SiPeCaM files",
      author="CONABIO",
      packages=['simex'],
      install_requires = [
                          "guano",
                          "pillow",
                          "hachoir",
                          ],
      entry_points = {
          'console_scripts': [
                              cli_list,
                              cli_extract_sn_coord,
                              cli_extract_met_and_ing
                              ]
                     }
      )