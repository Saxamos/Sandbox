# Features from music

- From a video, split audio sources
    + https://github.com/deezer/spleeter
    
- From audio get time intervals with speech
    + pydub

- From audio with language use speech to text
    + speech_recognition + api
    + https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426

- From audio get viz
    - https://pythonfundu.blogspot.com/2019/03/realtime-audio-visualization-in-python.html
    - https://stackoverflow.com/questions/6356749/music-analysis-and-visualization

- From audio voice use language detection
    - https://github.com/twerkmeister/iLID
    - https://arxiv.org/abs/1910.04269
    - https://github.com/rezasugiarto/Spoken-Language-Identification
    - https://github.com/sahilbadyal/language-detection-speech-using-dnn
    - https://www.kaggle.com/toponowicz/spoken-language-identification

- From audio get key moment
    - https://www.kaggle.com/pray199/spoken-languange-visualization
    - https://www.kaggle.com/c/birdsong-recognition/discussion/172573
    - https://medium.com/prathena/the-dummys-guide-to-mfcc-aceab2450fd


# Mail from MuseMind

"Nous avons illustré sur différentes vidéos le rendu sonore que nous pourrions obtenir avec un flot 
totalement automatisé.

Le compromis automatisation / qualité nous semble tout à fait bon.
(Pour ces exemples, les timings de découpe sont approximatifs, car nous ne disposions pas des point précis)

Cela nécessite quelques développements de notre côté, le traitement apporté étant différent de celui habituel.

Pourrions-nous discuter ensemble de comment réaliser ces activités ainsi que la priorisation (planning).

Cela pourrait se faire au moyen d’un PoC avec :
- une première étape où MuseMind réaliserait une solution technique automatique capable de restituer à 
Aive une bande sonore sur la base d’une vidéo et d’un fichier de timings des points de coupe
- une deuxième étape consisterait en la définition d’une architecture commune où traitement vidéo et 
audio pourraient être parallélisé

Reste à voir comment traiter les quelques cas de figure où des retouches manuelles seraient nécessaires et 
que cela soit acceptable pour le client final.