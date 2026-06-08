import os
import pathlib

# Define the absolute target root directory (Set to Further_Mathematics)
TARGET_ROOT = pathlib.Path("/Users/evanward/Documents/GitHub/maths-fmaths-portal/CCEA_Portal/Further_Mathematics")

# The exact required internal structure for every single sub-topic
INTERNAL_FOLDERS = [
    "mermaid", 
    "svg", 
    "tikz", 
    "widgets", 
    "Enrichment", 
    "Practice_Questions", 
    "Flashcards"
]

INTERNAL_FILES = [
    "{slug}_Lesson.md",
    "Manifest.md",
    "Packaging_Instructions.md",
    "Source_Reference.md"
]

# The Complete CCEA Further Mathematics Master Map - Numbered & Capitalized
PORTAL_STRUCTURE = {
    "AS_Level": {
        "FAS1_Pure_Mathematics": {
            "01_Further_Algebra_and_Functions": [
                "01_Roots_and_Coefficients_of_Quadratics"
            ],
            "02_Complex_Numbers": [
                "01_Complex_Arithmetic_and_Equations",
                "02_Argand_Diagrams_and_Modulus_Argument_Form",
                "03_Loci_in_the_Argand_Diagram"
            ],
            "03_Matrices": [
                "01_Matrix_Arithmetic_and_Transformations",
                "02_Determinants_and_Inverses",
                "03_Solving_Simultaneous_Equations"
            ],
            "04_Vectors": [
                "01_Lines_and_Planes_in_3D",
                "02_Scalar_Product_and_Intersections",
                "03_Vector_Product_and_Applications"
            ]
        },
        "FAS2_Applied_Mathematics": {
            "01_Hookes_Law": [
                "01_Elastic_Strings_and_Springs"
            ],
            "02_Work_and_Energy": [
                "01_Work_Energy_and_Conservation"
            ],
            "03_Power": [
                "01_Power_and_Motion"
            ],
            "04_Circular_Motion": [
                "01_Horizontal_Circular_Motion"
            ],
            "05_Further_Particle_Equilibrium": [
                "01_Equilibrium_with_Friction_and_Elasticity"
            ],
            "06_Resultant_and_Relative_Velocity": [
                "01_Relative_Velocity_and_Interception"
            ],
            "07_Further_Circular_Motion_Vertical": [
                "01_Vertical_Circular_Motion"
            ],
            "08_Gravitation": [
                "01_Universal_Gravitation_and_Satellites"
            ],
            "09_Dimensions": [
                "01_Dimensional_Analysis"
            ],
            "10_Sampling": [
                "01_Sampling_Techniques_and_Critique"
            ],
            "11_Probability": [
                "01_Permutations_Combinations_and_Probability"
            ],
            "12_Statistical_Distributions": [
                "01_Discrete_Continuous_and_Poisson_Distributions"
            ],
            "13_Bivariate_Distributions": [
                "01_Correlation_Regression_and_Extrapolation"
            ],
            "14_Group_Theory": [
                "01_Group_Axioms_Subgroups_and_Isomorphism"
            ],
            "15_Graph_Theory": [
                "01_Graphs_Trees_and_Traversability"
            ],
            "16_Algorithms_on_Graphs": [
                "01_Critical_Paths_and_Shortest_Paths"
            ],
            "17_Recurrence_Relationships": [
                "01_Recurrence_Models_and_Solutions"
            ],
            "18_Boolean_Algebra": [
                "01_Truth_Tables_and_Equivalence"
            ]
        }
    },
    "A2_Level": {
        "FA21_Pure_Mathematics": {
            "01_Proof": [
                "01_Mathematical_Induction"
            ],
            "02_Further_Algebra_and_Functions": [
                "01_Partial_Fractions_and_Summation_of_Series",
                "02_Maclaurin_Series_and_Small_Angles"
            ],
            "03_Complex_Numbers": [
                "01_De_Moivres_Theorem_and_Exponential_Form",
                "02_Nth_Roots_and_Roots_of_Unity"
            ],
            "04_Further_Calculus": [
                "01_Improper_Integrals_and_Inverse_Trig",
                "02_Reduction_Formulae_and_Integration_by_Parts"
            ],
            "05_Polar_Coordinates": [
                "01_Polar_Coordinates_Curves_and_Area"
            ],
            "06_Hyperbolic_Functions": [
                "01_Definitions_Graphs_and_Calculus",
                "02_Inverse_Hyperbolic_Functions"
            ],
            "07_Differential_Equations": [
                "01_First_Order_and_Integrating_Factors",
                "02_Second_Order_Differential_Equations"
            ]
        },
        "FA22_Applied_Mathematics": {
            "01_Simple_Harmonic_Motion": [
                "01_SHM_and_Oscillations"
            ],
            "02_Damped_Oscillations": [
                "01_Modelling_Damped_Oscillations"
            ],
            "03_Centre_of_Mass": [
                "01_Centre_of_Mass_and_Suspension"
            ],
            "04_Frameworks": [
                "01_Light_Pin_Jointed_Frameworks"
            ],
            "05_Further_Circular_Motion_Banked": [
                "01_Banked_Corners_Sliding_Overturning"
            ],
            "06_Further_Kinematics": [
                "01_Kinematics_3D_and_Variable_Acceleration"
            ],
            "07_Further_Centre_of_Mass": [
                "01_Calculus_and_Toppling"
            ],
            "08_Force_Systems_in_Two_Dimensions": [
                "01_Resultants_and_Equivalent_Systems"
            ],
            "09_Restitution": [
                "01_Elastic_Collisions_and_Restitution"
            ],
            "10_Linear_Combinations": [
                "01_Expectation_Variance_and_Normal_Combinations"
            ],
            "11_Sampling_and_Estimation": [
                "01_Central_Limit_Theorem_and_Confidence_Intervals"
            ],
            "12_The_T_Distribution": [
                "01_T_Tests_and_Confidence_Intervals"
            ],
            "13_Chi_Squared_Tests": [
                "01_Goodness_of_Fit_and_Contingency_Tables"
            ],
            "14_Counting": [
                "01_Inclusion_Exclusion_and_Rook_Polynomials"
            ],
            "15_Graph_Theory_Advanced": [
                "01_Matchings_Flows_and_Colourings"
            ],
            "16_Algorithms_on_Graphs_Advanced": [
                "01_PERT_Simplex_and_Nearest_Neighbour"
            ],
            "17_Generating_Functions": [
                "01_Generating_Functions_and_Combinatorics"
            ],
            "18_Group_Theory_Advanced": [
                "01_Symmetry_Groups_and_Polyas_Theorem"
            ]
        }
    }
}

def build_complete_shell():
    print(f"Initializing complete CCEA Further Mathematics portal build at: {TARGET_ROOT}\n")
    
    for level, units in PORTAL_STRUCTURE.items():
        for unit, chapters in units.items():
            for chapter, sub_topics in chapters.items():
                for sub_topic in sub_topics:
                    
                    # Construct the full directory path
                    topic_path = TARGET_ROOT / level / unit / chapter / sub_topic
                    topic_path.mkdir(parents=True, exist_ok=True)
                    
                    # Create the internal asset and pillar folders
                    for folder in INTERNAL_FOLDERS:
                        (topic_path / folder).mkdir(exist_ok=True)
                        
                    # Generate a clean slug for the lesson file (e.g., "01_Roots_and_Coefficients" -> "Roots_and_Coefficients")
                    slug_parts = sub_topic.split("_")[1:] 
                    clean_slug = "_".join(slug_parts)
                    
                    for file_template in INTERNAL_FILES:
                        file_name = file_template.format(slug=clean_slug)
                        file_path = topic_path / file_name
                        file_path.touch()
                        
                    print(f"Created: {level}/{unit}/{chapter}/{sub_topic}/")

if __name__ == "__main__":
    try:
        build_complete_shell()
        print("\nSUCCESS: The complete CCEA Further Mathematics specification shell has been built.")
    except Exception as e:
        print(f"An error occurred: {e}")