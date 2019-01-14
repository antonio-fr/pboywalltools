
iv=$(echo -ne '12345678b0z2345n'|xxd -pu);
pwd=$(echo -ne '03012009'|xxd -pu);
echo 'mq+cC6Ax2+8R8LAnEWgQnA=='|openssl enc -a -d -aes-128-cbc -K $pwd -iv $iv && echo '';

