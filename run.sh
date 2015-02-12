keychain ~/.ssh/id_rsa

ssh $1@$2 cat $3 | zgrep -iA0 'Terminado' --color | tail -n 1
