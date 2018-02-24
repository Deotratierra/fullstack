## API wrappers síncronos
Si el rendimiento es algo que no nos interesa especialmente en el desarrollo de un puente hacia una API, lo suyo es realizar un wrapper síncrono para facilitar su uso a los programadores no experimentados en bibliotecas asíncronas.

### Python
Mi recomendación es usar la biblioteca `urllib` (si, la primera). Es muy simple de usar cuando te acostumbras, no necesita dependencia alguna y es compatible en todas las versiones de Python.