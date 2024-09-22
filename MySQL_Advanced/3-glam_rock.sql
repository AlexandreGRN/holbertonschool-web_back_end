-- script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, IFNULL(split, 2020) - formed AS lifespan
-- select band name and lifespan
FROM metal_bands
-- from metal_bands
WHERE style LIKE '%Glam rock%'
-- where style is like glam rock
ORDER BY lifespan DESC;
