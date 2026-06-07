# AS2MeasuresLocationSpreadMermaid-008

## Asset ID
`AS2MeasuresLocationSpreadMermaid-008`

## Purpose
Show variance as mean of squares minus square of mean, and standard deviation as the square root of variance.

```mermaid
flowchart TD
    A["Need a measure of spread using all values"] --> B["Variance"]
    B --> C["Idea:<br/>average squared distance from the mean"]
    B --> D["Shortcut:<br/>mean of squares - square of mean"]
    D --> E["Listed data:<br/>\\(\\sigma^2=\\frac{\\sum x^2}{n}-\\bar{x}^2\\)"]
    D --> F["Frequency data:<br/>\\(\\sigma^2=\\frac{\\sum fx^2}{\\sum f}-\\bar{x}^2\\)"]
    E --> G["Standard deviation"]
    F --> G
    G --> H["\\(\\sigma=\\sqrt{\\sigma^2}\\)"]
    H --> I["Larger SD means more spread"]
    H --> J["Smaller SD means values are more clustered"]
```
