for word in `cat utt`;
do
    formatted=`echo $word | tr -dc '[:alnum:]' | tr  '[:lower:]' '[:upper:]'`
    echo -n $formatted ' '
done