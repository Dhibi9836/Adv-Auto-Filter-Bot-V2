if [ -z $UPSTREAM_REPO ]

then

  echo "Cloning main Repository"

  git clone https://github.com/Dhibi9836/Adv-Auto-Filter-Bot-V2
else

  echo "Cloning Custom Repo from $UPSTREAM_REPO "

  git clone $UPSTREAM_REPO /main

fi

cd /Eva

pip3 install -U -r requirements.txt

echo "Starting Bot...."

python3 bot.py

Footer

© 2022 GitHub, Inc.

Footer navigation

Terms

Privacy
