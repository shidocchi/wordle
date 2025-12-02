# wordle

wordle solver

- 英単語当てゲーム wordle の解法支援プログラムです
- 5文字の「単語」「ヒット＆ブローの文字列」を入力すると、一致する英単語を一覧表示します

## what is wordle?

https://www.powerlanguage.co.uk/wordle/

## preparing

```
$ pip install git+https://github.com/shidocchi/wordle.git

$ wget https://slc.is/data/wordles.txt
```

## play wordle with solver

```
$ python -m wordle

  guess(1): ready
hitblow(1): -B-B-
 possib(1): bided bides bidet bield biked biled biped bleed blend blued boded bodes bodge bodle boked boned booed bowed boxed budge bused cided cides cited clied
clued codec coded coden codes codex coked coled coned cooed coped cosed coted coved cowed coxed cozed cubed dhole diced dices didie diebs diels diene diets diked
dikes dimes dined dines dinge diode disme dited dites dived dives dixie dizen dobes dobie dodge doeks doest doeth doges dogie dolce doled doles domed domes donee
donne dooce doole doped dopes dosed doseh doses doted dotes douce douse doved doven doves dovie dowed dowel dowie dowle dowse doxed doxes doxie dozed dozen dozes
duces duded dudes duels duets duett duked dukes dulce dules dulse dunce dunes duped dupes duple duvet duxes dweeb dwell dwelt dwile dwine ebbed eched edged edges
edict edile edits educe educt effed egged eidos eiked eldin elfed embed emend ended endew endow endue ephod equid euked ewked fides fidge field fiend fifed fiked
filed fined fixed fjeld flied flued foxed fudge fumed fused fuzed gibed gived gleed glued godet gudes hided hides hiked hived hohed hoied hoked holed homed honed
hoped hosed hoved hoxed iched idees ident idled idles igged imbed imped indew index indie indue inked inned isled ivied jibed jived jobed jodel joked joled jowed
judge juked kidel kidge kited kneed liked limed lined lited lived lobed loden lodes lodge lomed looed loped losed loued loved lowed loxed lubed ludes luged luted
luxed midge miked mimed mined mixed model modem modes modge moled mooed moped mosed moted moved mowed mozed mudge muled mused muted muxed nided nides nixed nodes
nosed noted nowed nudes nudge nudie nuked obied odeon odeum offed ogeed ogled oiled olden oldie onned oohed ooped oozed opted ouped outed owled owned piend piked
piled pined piped pized plied podex podge pohed poked poled pooed posed poted poxed pseud pudge puked puled pwned scend sdein shend shied shoed sided sides sidhe
sidle sield siled sined siped sited sized skeed skied slued sneed soled sowed speed speld spend spied spued steed stend stied sused sweed theed ticed tided tides
tiled timed tined todde toged toked toled toned toped tosed toted towed tozed tsked tubed tuned tweed ugged ummed umped unbed undee undue unfed unked unled unwed
upend upled upped viced video vined vised voled voted vowed widen wides wield wifed wiled wined wiped wised wited wived wodge wooed wowed zoned

  guess(2): spend
hitblow(2): --HHB
 possib(2): diene ident

  guess(3):
[p]op / [c]lear / e[x]it? x
```

## 雑感

* ここ数日、淡々と頭の体操として続けてきましたが、そろそろ潮時かな

    * TVメディアが紹介し始めた
    * そもそも難読化やAPIを使わず正解をソースコードに埋め込んでいるので、チートしてる人が一定数いる
    * チート方法も堂々と紹介しているサイトが複数ある
    * 「コピーアプリが一掃された」とのニュースがあるが、こんなゲーム腐るほどあって当然で、なぜここが本家面して他をコピー呼ばわりするのか疑問
    * 知っている英単語もあるがマニアックなものが多く、「普通こっちだろ」と思ったら逆だったことが結構ある
    * Steamに似た名前だけど別のゲーム (Wordle4) があり、そちらの方が知っている英単語ばかりなのでストレスがない
    * 自分は、すでにJavaScriptコードを読んでいるので、そこに正解が含まれていることは知っていてファイルに保存してあるが、読まないようにしている
    * あえてチートをせずに続けているのは、英単語の勉強とプログラミングの練習になるから
    * 重複文字がある状況でHit-and-Blowの判定をするのは難しくて、今でもプログラムが正しく動作しているか自信がない
    * あまり英単語の勉強にならないような難しい単語が続くようであれば、本家を解くのはやめて、自分でWordleクローンでも作るかもしれない
    * もちろんそれで商売は考えず、あくまで英単語の勉強とプログラミングの練習が目的であり、コピー呼ばわりされる筋合いはない
