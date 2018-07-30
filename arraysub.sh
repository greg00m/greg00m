#!/bin/bash

declare -a gregs_array

gregs_array=("You cannot shake hands with a clenched fist.\n" "Whoever is happy will make others happy too.\n" "Let us be grateful to the people who make us happy.\n" "Very little is needed to make a life happy.\n" "Be happy for this moment. This moment is your life.\n")

echo -e ${gregs_array[0]//happy/sloppy/n}
echo -e ${gregs_array[1]//happy/sloppy}
echo -e ${gregs_array[2]//happy/slpppy}
echo -e ${gregs_array[3]//happy/sloppy}
echo -e ${gregs_array[4]//happy/sloppy}




