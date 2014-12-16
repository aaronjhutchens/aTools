#!/bin/bash


# Parse options, currently taking -3 "dir" and -n "limit".  Now also taking -s sourceDir
trailingSlash='\/$'
while getopts  ":d:n:s:" opt; do
        case $opt in
                d)
                        if [ -d "$OPTARG" ] && [[ $OPTARG =~ $trailingSlash ]]
                        then
                                directory="$OPTARG"
                        else
                                echo "-d must be an existing directory WITH A TRAILING SLASH!"
                                exit 1
                        fi
                        ;;
                n)
                        if [ "$OPTARG" -gt 1 ]
                        then
                                ((limit="$OPTARG"))
                        else
                                echo "-n must be an integer larger than 1"
                                exit 1
                        fi
                        ;;
                s)
                        if [ -d "$OPTARG" ] && [[ $OPTARG =~ $trailingSlash ]]
                        then
                                sourceDir="$OPTARG"
                        else
                                echo "-s must be the source directory, WITH A TRAILING SLASH!"
                                exit 1
                        fi
                        ;;
                \?)
                        echo "Invalid option"
                        ;;
                :)
                        echo "Option requires an argument"
                        ;;
        esac
done

rotate(){
# Grab the NEWEST file from the source directory, move it to the $directory, and then touch it to update its timestamp.
        sourceFile=$(/bin/ls -lAt $sourceDir |head -n 2 |awk '{if (NR>1) print $NF}')
        cp -r $sourceDir$sourceFile $directory
        touch $directory$sourceFile
}
getCount(){
# Just get a count of files in $directory
        ((numFiles=$(ls -lAht $directory |wc -l) - 1))
}

getOldest(){
# Get the oldest file in $directory
        oldestFile=$(/bin/ls -lAt $directory |tail -n 1 |awk '{print $NF}')
}
trimFat(){
# Cull the herd
        getCount
        while [ "$numFiles" -gt "$limit" ]
        do
                getOldest
                rm -rf $directory/$oldestFile
                getCount
        done
}

if [ -e "$sourceDir" ]
then
        rotate
else
        echo "Skipping rotation!"
fi
trimFat

