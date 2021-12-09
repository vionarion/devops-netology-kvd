 Будут игнорироваться все файлы в имени которых есть буквосочетание override.tf
override.tf.json crash.log terraform.rc .terraformrc 

будут игнорироваться *_override.tf
*_override.tf.json *.tfvars *.tfstate
'*.tfstate.*' директория '**/.terraform/*' (локальная директория)
