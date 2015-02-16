keychain ~/.ssh/id_rsa

ssh $1@$2 zcat -f $3 | zgrep -iA0 'Terminado' --color | tail -n 1
