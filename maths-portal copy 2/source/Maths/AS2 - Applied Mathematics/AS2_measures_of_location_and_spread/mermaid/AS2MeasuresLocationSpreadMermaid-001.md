# AS2MeasuresLocationSpreadMermaid-001

## Asset ID
`AS2MeasuresLocationSpreadMermaid-001`

## Source
CCEA AS2-DPI specification map; Chapter 2 Measures of Location & Spread transcript; Phase 1 lesson section: Measures of Location and Measures of Spread.

## Purpose
Show central tendency as part of location, and separate it from spread.

```mermaid
flowchart TD
    A["Measures used to summarise data"] --> B["Measures of Location<br/>single values describing a position in a data set"]
    A --> C["Measures of Spread<br/>describe how spread out the data are"]
    B --> D["Measures of Central Tendency<br/>describe the centre of the data"]
    D --> E["Mean<br/>\\(\\bar{x}\\)"]
    D --> F["Median<br/>\\(Q_2\\)"]
    D --> G["Mode<br/>modal value"]
    B --> H["Other Location Measures"]
    H --> I["Minimum"]
    H --> J["Maximum"]
    H --> K["Quartiles<br/>\\(Q_1,Q_2,Q_3\\)"]
    H --> L["Percentiles and Deciles<br/>boundary-risk enrichment"]
    C --> M["Range<br/>maximum - minimum"]
    C --> N["Interquartile Range<br/>\\(Q_3-Q_1\\)"]
    C --> O["Variance<br/>average squared distance from mean"]
    C --> P["Standard Deviation<br/>square root of variance"]
```
