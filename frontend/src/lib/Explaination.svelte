<scrip>

</scrip>
<body class="card p-8 text-center m-5 ">
        <h1 class="text-2xl font-semibold mb-4">Exploring Sentiment Analysis with NLTK's VADER Lexicon</h1>
        
        <h2 class="text-lg font-semibold mb-2">Q. What is VADER?</h2>
        <p class=" mb-4">A. VADER (Valence Aware Dictionary and sEntiment Reasoner) is an open source rule-based lexicon model for sentiment analysis provided by NLTK.</p>

        <h2 class="text-lg font-semibold mb-2">Q. What does lexicon mean?</h2>
        <p class=" mb-4">A. Lexicon here defines a set of words which have specific weightages for negativity/positivity/neutrality of a sentence.</p>

        <p class=" mb-4">To understand what it does, we need to first understand its limitations.</p>

        <h2 class="text-lg font-semibold mb-2">Limitations:</h2>
        <p class=" mb-4">Due to the lexicon-based model, it has no context awareness; thus, sarcasm or other mild-worded insults can be marked as positive.</p>
        <p class=" mb-4">Example: "Your capacity to be confidently incorrect is astonishing."</p>
        <p> See what I did there? I used multiple high-polarity words. This sabotages the machine to think it's not negative.</p>
        <p> The final compound sentiment is the final weighted sum of the weightages for the specific words in the corpus.</p>
</body>