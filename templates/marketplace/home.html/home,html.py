<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Artist Marketplace</title>
</head>
<body>
    <h1>Welcome to the Artist Marketplace</h1>
    <h2>Artwork Listings</h2>
    <ul>
        {% for artwork in artworks %}
            <li>{{ artwork.title }} - ${{ artwork.price }}</li>
        {% empty %}
            <li>No artworks available.</li>
        {% endfor %}
    </ul>
</body>
</html>
