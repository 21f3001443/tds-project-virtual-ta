## Nominatim API with Python

[![Nominatim Open Street Map with Python](https://i.ytimg.com/vi_webp/f0PZ-pphAXE/sddefault.webp)](https://youtu.be/f0PZ-pphAXE
<youtube_summary>This tutorial explains how to use the Geocoding API via the Nominatim service in the geopy.geocoders Python library to extract detailed information from a textual address input. By typing any address as text (e.g., "Eiffel Tower" or "IIT Madras"), the API returns data such as latitude, longitude, the type of place, and the full correct address, similar to how Google Maps refines approximate inputs. Nominatim is an open-source geocoding tool provided by OpenStreetMap, analogous to Google Maps but open-source. The geopy library, which includes Nominatim, needs to be installed locally but is pre-installed on Google Colab. The tutorial demonstrates importing Nominatim, creating a geocoder object with a user agent, and using the geocode function to input an address. The returned location object behaves like a JSON/dictionary, providing extensive details such as bounding box coordinates, place classification (e.g., tourism, amenity), place type (e.g., museum, university), images, license info, and internal IDs. Examples show how searching "Eiffel Tower" yields its precise coordinates and classification as a tourist attraction, while searching "IIT Madras" returns its exact address in Tamil Nadu, India, and identifies it as a university under the amenity class. This information can be very useful for various applications. The tutorial concludes by encouraging viewers to use Nominatim for extracting rich geocoding data from simple text inputs.</youtube_summary>
)

You'll learn how to get the latitude and longitude of any city from the Nominatim API.

- **Introduction to Nominatim**: Understand how Nominatim, from OpenStreetMap, works similarly to Google Maps for geocoding.
- **Installation and Import**: Learn to install and import [geopy](https://geopy.readthedocs.io/) and [nominatim](https://nominatim.org/).
- **Using the Locator**: Create a locator object using Nominatim and set up a user agent.
- **Geocoding an Address**: Use `locator.geocode` to input an address (e.g., Eiffel Tower) and fetch geocoded data.
- **Extracting Data**: Access detailed information like latitude, longitude, bounding box, and accurate address from the JSON response.
- **Classifying Locations**: Identify the type of place (e.g., tourism, university) using the response data.
- **Practical Example**: Geocode "IIT Madras" and retrieve its full address, type (university), and other relevant information.

Here are links and references:

- [Geocoding using Nominatim - Notebook](https://colab.research.google.com/drive/1-vvP-UyMjHgBqc-hdsUhm3Bsbgi7oO6g)
- Learn about the [`geocoders` module in the `geopy` package](https://geopy.readthedocs.io/)
- Learn about the [`nominatim` package](https://nominatim.org/release-docs/develop/api/Overview/)
- If you get a HTTP Error 403 from Nominatim, use your email ID or your name instead of "myGeocoder" in `Nominatim(user_agent="myGeocoder")`
