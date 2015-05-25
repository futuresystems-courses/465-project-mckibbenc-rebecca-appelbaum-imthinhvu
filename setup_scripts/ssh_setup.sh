# Create a key pair for the ubuntu user
echo -ne '\n' | ssh-keygen -t rsa -P ""
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Add the public key to all other nodes
echo "StrictHostKeyChecking=no" > ~/.ssh/config
getArray "nodes.txt"
for node in "${array[@]}"
do
    ssh-copy-id ubuntu@$node
done


array=()

getArray() {
    i=0
    while read line
    do
        array[i]=$line
        i=$(($i + 1))
    done < $1
}

