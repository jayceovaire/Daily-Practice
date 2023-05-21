function lastPetalPhrase(petals) {
  const phrases = [
    "I love you",
    "a little",
    "a lot",
    "passionately",
    "madly",
    "not at all"
  ];

  const phraseIndex = (petals - 1) % phrases.length;
  return phrases[phraseIndex];
}

