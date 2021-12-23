1. Нашел полный хеш (aefead2207ef7e2aa5dc81a34aedf0cad4c32545) и комментарий коммита (Update CHANGELOG.md), хеш которого 
начинается на aefea.
При помощи комманды - git log aefea

2. Коммит 85024d3 соответствует тегу (tag: v0.12.23)

При помощи комманды - git log 85024d3

5. У коммита b8d720 Напишите их хеши, 2 родителя.
Их хеши:

>56cd7859e05c36c06b56d013b55a252d0bb7e158 ---
9ea88f22fc6269854151c571162c5bcf958bee2b

При помощи комманды - git log b8d720 -p

4. Перечисляю все хеши и комментарии коммитов которые были сделаны между тегами v0.12.23 и v0.12.24:


>33ff1c03bb960b332be3af2e333462dde88b279e ,v0.12.24
> 
> b14b74c4939dcab573326f4e3ee2a62e23e12f89 ,[Website] vmc provider links
> 
> 3f235065b9347a758efadc92295b540ee0a5e26e ,Update CHANGELOG.md
> 
> 6ae64e247b332925b872447e9ce869657281c2bf ,registry: Fix panic when server is unreachable
> 
> 5c619ca1baf2e21a155fcdb4c264cc9e24a2a353 ,website: Remove links to the getting started guide's old location
> 
> 06275647e2b53d97d4f0a19a0fec11f6d69820b5 ,Update CHANGELOG.md
> 
> d5f9411f5108260320064349b757f55c09bc4b80 ,command: Fix bug when using terraform login on Windows
> 
> 4b6d06cc5dcb78af637bbb19c198faff37a066ed ,Update CHANGELOG.md

При помощи комманды - git log v0.12.24 -s

5. Коммит в котором была создана функция func providerSource 
>commit 5af1e6234ab6da412fb8637393c5a17a1b293663

При помощи комманды - git grep providerSource

6. Все коммиты в которых была изменена функция globalPluginDirs:

>commit 35a058fb3ddfae9cfee0b3893822c9a95b920f4c
> 
> commit c0b17610965450a89598da491ce9b6b5cbd6393f

При помощи комманды - git grep globalPluginDirs

7. Автор функции synchronizedWriters

>James Bardin <j.bardin@gmail.com>

При помощи комманды - git grep synchronizedWriters