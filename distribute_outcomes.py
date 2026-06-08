import os
import pathlib

# --- 1. CONFIGURATION PATHS ---
TARGET_ROOT = pathlib.Path("/Users/evanward/Documents/GitHub/maths-fmaths-portal/CCEA_Portal")

# The exact paths to your legacy specification documents
MATHS_SPEC_PATH = pathlib.Path("/Users/evanward/Documents/GitHub/maths-fmaths-portal/maths-portal copy 2/source/Specifications/CCEA_GCE_Mathematics_Specification_Map.md")
FMATHS_SPEC_PATH = pathlib.Path("/Users/evanward/Documents/GitHub/maths-fmaths-portal/maths-portal copy 2/source/Specifications/CCEA_GCE_Further_Mathematics_Specification_Map.md")

# --- 2. PARSING ENGINE ---
def parse_spec_file(filepath):
    """Reads the markdown tables and extracts LO data into a dictionary."""
    lo_data = {}
    if not filepath.exists():
        print(f"ERROR: Could not find {filepath}. Please check the path!")
        return lo_data

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('|') and '-LO' in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 6 and parts[1].startswith(('AS', 'A2', 'FAS', 'FA2')):
                    lo_id = parts[1]
                    lo_data[lo_id] = {
                        'specification': parts[2],
                        'elaboration': parts[3],
                        'student_meaning': parts[4],
                        'boundaries': parts[5]
                    }
    return lo_data

# --- 3. THE COMPLETE ALLOCATION DICTIONARY ---
FOLDER_MAPPING = {
    # --- AS1 PURE MATHEMATICS ---
    "Mathematics/AS_Level/AS1_Pure_Mathematics/01_Algebra_and_Functions/01_Indices_and_Surds": ["AS1-AF-LO001", "AS1-AF-LO002"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/01_Algebra_and_Functions/02_Quadratics_and_Discriminant": ["AS1-AF-LO003", "AS1-AF-LO004", "AS1-AF-LO005", "AS1-AF-LO006"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/01_Algebra_and_Functions/03_Simultaneous_Equations": ["AS1-AF-LO007", "AS1-AF-LO008"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/01_Algebra_and_Functions/04_Inequalities": ["AS1-AF-LO009"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/01_Algebra_and_Functions/05_Polynomials_and_Theorems": ["AS1-AF-LO010", "AS1-AF-LO011"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/01_Algebra_and_Functions/06_Curve_Sketching_and_Intersections": ["AS1-AF-LO012", "AS1-AF-LO013", "AS1-AF-LO014", "AS1-AF-LO015"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/01_Algebra_and_Functions/07_Graph_Transformations": ["AS1-AF-LO016"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/02_Coordinate_Geometry/01_Straight_Lines": ["AS1-CG-LO001", "AS1-CG-LO002", "AS1-CG-LO003", "AS1-CG-LO004"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/02_Coordinate_Geometry/02_Circles_and_Tangents": ["AS1-CG-LO005", "AS1-CG-LO006", "AS1-CG-LO007", "AS1-CG-LO008"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/03_Sequences_and_Series/01_Binomial_Expansion": ["AS1-SS-LO001", "AS1-SS-LO002"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/04_Trigonometry/01_Definitions_and_Graphs": ["AS1-TRIG-LO001", "AS1-TRIG-LO004"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/04_Trigonometry/02_Sine_Cosine_Rules_and_Area": ["AS1-TRIG-LO002", "AS1-TRIG-LO003"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/04_Trigonometry/03_Trigonometric_Identities": ["AS1-TRIG-LO005", "AS1-TRIG-LO006"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/04_Trigonometry/04_Solving_Trigonometric_Equations": ["AS1-TRIG-LO007"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/05_Exponentials_and_Logarithms/01_Exponential_Functions_and_Graphs": ["AS1-EXPLOG-LO001", "AS1-EXPLOG-LO002"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/05_Exponentials_and_Logarithms/02_Logarithmic_Functions_and_Graphs": ["AS1-EXPLOG-LO003", "AS1-EXPLOG-LO004", "AS1-EXPLOG-LO005"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/05_Exponentials_and_Logarithms/03_Laws_of_Logarithms": ["AS1-EXPLOG-LO006"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/05_Exponentials_and_Logarithms/04_Solving_Equations_and_Inequalities": ["AS1-EXPLOG-LO007", "AS1-EXPLOG-LO008"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/05_Exponentials_and_Logarithms/05_Exponential_Modelling": ["AS1-EXPLOG-LO009", "AS1-EXPLOG-LO010"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/06_Differentiation/01_Gradients_and_Limits": ["AS1-DIFF-LO001", "AS1-DIFF-LO002", "AS1-DIFF-LO003"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/06_Differentiation/02_Differentiation_Rules_and_Second_Derivatives": ["AS1-DIFF-LO004", "AS1-DIFF-LO005", "AS1-DIFF-LO006"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/06_Differentiation/03_Tangents_Normals_and_Stationary_Points": ["AS1-DIFF-LO007"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/06_Differentiation/04_Increasing_and_Decreasing_Functions": ["AS1-DIFF-LO008"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/07_Integration/01_Indefinite_Integration": ["AS1-INT-LO001", "AS1-INT-LO002"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/07_Integration/02_Definite_Integration_and_Area": ["AS1-INT-LO003", "AS1-INT-LO004"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/08_Vectors/01_Vectors_in_Two_Dimensions": ["AS1-VEC-LO001", "AS1-VEC-LO002", "AS1-VEC-LO003"],
    "Mathematics/AS_Level/AS1_Pure_Mathematics/08_Vectors/02_Position_Vectors_and_Distance": ["AS1-VEC-LO004", "AS1-VEC-LO005"],

    # --- AS2 APPLIED MATHEMATICS ---
    "Mathematics/AS_Level/AS2_Applied_Mathematics/01_Quantities_and_Units/01_SI_and_Derived_Units": ["AS2-QUNITS-LO001", "AS2-QUNITS-LO002"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/02_Kinematics/01_Language_and_Graphs_of_Motion": ["AS2-KIN-LO001", "AS2-KIN-LO002"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/02_Kinematics/02_Constant_Acceleration_1D": ["AS2-KIN-LO003"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/02_Kinematics/03_Constant_Acceleration_2D_Vectors": ["AS2-KIN-LO004"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/03_Forces_and_Newtons_Laws/01_Newtons_First_Law_and_Resolving_Forces": ["AS2-FORCES-LO001", "AS2-FORCES-LO002", "AS2-FORCES-LO003"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/03_Forces_and_Newtons_Laws/02_Newtons_Second_Law_and_Gravity": ["AS2-FORCES-LO004", "AS2-FORCES-LO005", "AS2-FORCES-LO006"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/03_Forces_and_Newtons_Laws/03_Newtons_Third_Law_and_Connected_Particles": ["AS2-FORCES-LO007", "AS2-FORCES-LO008"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/03_Forces_and_Newtons_Laws/04_Equilibrium_and_Statics": ["AS2-FORCES-LO009", "AS2-FORCES-LO013"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/03_Forces_and_Newtons_Laws/05_Friction": ["AS2-FORCES-LO010", "AS2-FORCES-LO011", "AS2-FORCES-LO012"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/04_Statistical_Sampling/01_Populations_Samples_and_Techniques": ["AS2-SAMP-LO001", "AS2-SAMP-LO002", "AS2-SAMP-LO003", "AS2-SAMP-LO004"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/05_Data_Presentation_and_Interpretation/01_Data_Diagrams_and_Measures_of_Spread": ["AS2-DPI-LO001", "AS2-DPI-LO002", "AS2-DPI-LO003", "AS2-DPI-LO009"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/05_Data_Presentation_and_Interpretation/02_Correlation_and_Regression": ["AS2-DPI-LO004", "AS2-DPI-LO005", "AS2-DPI-LO006", "AS2-DPI-LO007"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/05_Data_Presentation_and_Interpretation/03_Outliers_and_Cleaning_Data": ["AS2-DPI-LO008", "AS2-DPI-LO010"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/06_Probability/01_Probability_Laws_and_Events": ["AS2-PROB-LO001", "AS2-PROB-LO002"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/06_Probability/02_Combined_Probabilities": ["AS2-PROB-LO003"],
    "Mathematics/AS_Level/AS2_Applied_Mathematics/07_Statistical_Distributions/01_Binomial_Distribution": ["AS2-DIST-LO001", "AS2-DIST-LO002", "AS2-DIST-LO003"],

    # --- A21 PURE MATHEMATICS ---
    "Mathematics/A2_Level/A21_Pure_Mathematics/01_Algebra_and_Functions/01_Rational_Expressions_and_Partial_Fractions": ["A21-AF-LO001", "A21-AF-LO008"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/01_Algebra_and_Functions/02_Functions_Domain_Range_and_Composite": ["A21-AF-LO002", "A21-AF-LO003", "A21-AF-LO004"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/01_Algebra_and_Functions/03_Inverse_Functions": ["A21-AF-LO005"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/01_Algebra_and_Functions/04_Modulus_Functions": ["A21-AF-LO006"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/01_Algebra_and_Functions/05_Combinations_of_Transformations": ["A21-AF-LO007"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/01_Algebra_and_Functions/06_Functions_in_Modelling": ["A21-AF-LO009"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/02_Coordinate_Geometry/01_Parametric_Equations_and_Modelling": ["A21-CG-LO001", "A21-CG-LO002"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/03_Sequences_and_Series/01_Sequences_and_Sigma_Notation": ["A21-SS-LO001", "A21-SS-LO002"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/03_Sequences_and_Series/02_Arithmetic_Sequences_and_Series": ["A21-SS-LO003", "A21-SS-LO004", "A21-SS-LO005"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/03_Sequences_and_Series/03_Geometric_Sequences_and_Series": ["A21-SS-LO006", "A21-SS-LO007"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/03_Sequences_and_Series/04_Rational_Binomial_Expansion": ["A21-SS-LO008", "A21-SS-LO009"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/04_Trigonometry/01_Radians_Arc_Length_and_Sector_Area": ["A21-TRIG-LO001"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/04_Trigonometry/02_Reciprocal_and_Inverse_Trig_Functions": ["A21-TRIG-LO002", "A21-TRIG-LO003"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/04_Trigonometry/03_Sec_and_Cosec_Identities": ["A21-TRIG-LO004"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/04_Trigonometry/04_Compound_and_Double_Angle_Formulae": ["A21-TRIG-LO005", "A21-TRIG-LO006"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/04_Trigonometry/05_Rcos_Rsin_Forms": ["A21-TRIG-LO007"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/04_Trigonometry/06_Trigonometric_Proofs_and_Modelling": ["A21-TRIG-LO008", "A21-TRIG-LO009"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/05_Differentiation/01_Differentiating_Exp_Log_and_Trig": ["A21-DIFF-LO001", "A21-DIFF-LO002"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/05_Differentiation/02_Product_Quotient_and_Chain_Rules": ["A21-DIFF-LO003"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/05_Differentiation/03_Implicit_and_Parametric_Differentiation": ["A21-DIFF-LO004"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/05_Differentiation/04_Simple_Differential_Equations": ["A21-DIFF-LO005"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/06_Integration/01_Integrating_Standard_Functions": ["A21-INT-LO001"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/06_Integration/02_Area_Between_Curves_and_Limit_of_Sum": ["A21-INT-LO002", "A21-INT-LO003"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/06_Integration/03_Integration_by_Substitution_and_Parts": ["A21-INT-LO004"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/06_Integration/04_Integration_Using_Partial_Fractions": ["A21-INT-LO005"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/06_Integration/05_First_Order_Differential_Equations": ["A21-INT-LO006", "A21-INT-LO007"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/06_Integration/06_Volumes_of_Revolution": ["A21-INT-LO008"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/07_Numerical_Methods/01_Locating_Roots_and_Iteration": ["A21-NUM-LO001"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/07_Numerical_Methods/02_Newton_Raphson_Method": ["A21-NUM-LO002"],
    "Mathematics/A2_Level/A21_Pure_Mathematics/07_Numerical_Methods/03_Trapezium_Rule": ["A21-NUM-LO003", "A21-NUM-LO004"],

    # --- A22 APPLIED MATHEMATICS ---
    "Mathematics/A2_Level/A22_Applied_Mathematics/01_Kinematics/01_Calculus_in_Kinematics_1D_and_2D": ["A22-KIN-LO001", "A22-KIN-LO002"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/01_Kinematics/02_Motion_Under_Gravity_and_Projectiles": ["A22-KIN-LO003", "A22-KIN-LO004"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/02_Moments/01_Moments_and_Statics": ["A22-MOM-LO001"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/03_Impulse_and_Momentum/01_Impulse_Momentum_and_Collisions": ["A22-IMP-LO001", "A22-IMP-LO002"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/04_Probability/01_Conditional_Probability": ["A22-PROB-LO001", "A22-PROB-LO002"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/04_Probability/02_Probability_Modelling_and_Assumptions": ["A22-PROB-LO003"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/05_Statistical_Distributions/01_Normal_Distribution": ["A22-NORMAL-LO001", "A22-NORMAL-LO002", "A22-NORMAL-LO003"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/06_Statistical_Hypothesis_Testing/01_Language_of_Hypothesis_Testing": ["A22-HT-LO001", "A22-HT-LO002"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/06_Statistical_Hypothesis_Testing/02_Testing_Binomial_Proportions": ["A22-HT-LO003"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/06_Statistical_Hypothesis_Testing/03_Testing_Normal_Means": ["A22-HT-LO004"],
    "Mathematics/A2_Level/A22_Applied_Mathematics/06_Statistical_Hypothesis_Testing/04_Correlation_Testing": ["A22-HT-LO005"],

    # --- FAS1 PURE FURTHER MATHEMATICS ---
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/01_Further_Algebra_and_Functions/01_Roots_and_Coefficients_of_Quadratics": ["FAS1-FAF-LO001", "FAS1-FAF-LO002"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/02_Complex_Numbers/01_Complex_Arithmetic_and_Equations": ["FAS1-CN-LO001", "FAS1-CN-LO002", "FAS1-CN-LO003", "FAS1-CN-LO004", "FAS1-CN-LO005", "FAS1-CN-LO006"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/02_Complex_Numbers/02_Argand_Diagrams_and_Modulus_Argument_Form": ["FAS1-CN-LO007", "FAS1-CN-LO008", "FAS1-CN-LO009", "FAS1-CN-LO010", "FAS1-CN-LO011"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/02_Complex_Numbers/03_Loci_in_the_Argand_Diagram": ["FAS1-CN-LO012"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/03_Matrices/01_Matrix_Arithmetic_and_Transformations": ["FAS1-MAT-LO001", "FAS1-MAT-LO002", "FAS1-MAT-LO003", "FAS1-MAT-LO004", "FAS1-MAT-LO005", "FAS1-MAT-LO006"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/03_Matrices/02_Determinants_and_Inverses": ["FAS1-MAT-LO007", "FAS1-MAT-LO008", "FAS1-MAT-LO009", "FAS1-MAT-LO010", "FAS1-MAT-LO011", "FAS1-MAT-LO012"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/03_Matrices/03_Solving_Simultaneous_Equations": ["FAS1-MAT-LO013", "FAS1-MAT-LO014", "FAS1-MAT-LO015"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/04_Vectors/01_Lines_and_Planes_in_3D": ["FAS1-VEC-LO001", "FAS1-VEC-LO002", "FAS1-VEC-LO003"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/04_Vectors/02_Scalar_Product_and_Intersections": ["FAS1-VEC-LO004", "FAS1-VEC-LO005", "FAS1-VEC-LO006", "FAS1-VEC-LO007", "FAS1-VEC-LO008", "FAS1-VEC-LO009"],
    "Further_Mathematics/AS_Level/FAS1_Pure_Mathematics/04_Vectors/03_Vector_Product_and_Applications": ["FAS1-VEC-LO010", "FAS1-VEC-LO011", "FAS1-VEC-LO012"],

    # --- FAS2 APPLIED FURTHER MATHEMATICS ---
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/01_Hookes_Law/01_Elastic_Strings_and_Springs": ["FAS2-HOOKE-LO001", "FAS2-HOOKE-LO002"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/02_Work_and_Energy/01_Work_Energy_and_Conservation": ["FAS2-WENG-LO001", "FAS2-WENG-LO002", "FAS2-WENG-LO003", "FAS2-WENG-LO004"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/03_Power/01_Power_and_Motion": ["FAS2-POW-LO001", "FAS2-POW-LO002"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/04_Circular_Motion/01_Horizontal_Circular_Motion": ["FAS2-CM-LO001", "FAS2-CM-LO002", "FAS2-CM-LO003"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/05_Further_Particle_Equilibrium/01_Equilibrium_with_Friction_and_Elasticity": ["FAS2-FPE-LO001"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/06_Resultant_and_Relative_Velocity/01_Relative_Velocity_and_Interception": ["FAS2-RV-LO001", "FAS2-RV-LO002"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/07_Further_Circular_Motion_Vertical/01_Vertical_Circular_Motion": ["FAS2-FCM-LO001"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/08_Gravitation/01_Universal_Gravitation_and_Satellites": ["FAS2-GRAV-LO001", "FAS2-GRAV-LO002"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/09_Dimensions/01_Dimensional_Analysis": ["FAS2-DIM-LO001", "FAS2-DIM-LO002"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/10_Sampling/01_Sampling_Techniques_and_Critique": ["FAS2-SAMP-LO001", "FAS2-SAMP-LO002"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/11_Probability/01_Permutations_Combinations_and_Probability": ["FAS2-PROB-LO001", "FAS2-PROB-LO002", "FAS2-PROB-LO003", "FAS2-PROB-LO004"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/12_Statistical_Distributions/01_Discrete_Continuous_and_Poisson_Distributions": ["FAS2-DIST-LO001", "FAS2-DIST-LO002", "FAS2-DIST-LO003", "FAS2-DIST-LO004", "FAS2-DIST-LO005", "FAS2-DIST-LO006", "FAS2-DIST-LO007", "FAS2-DIST-LO008"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/13_Bivariate_Distributions/01_Correlation_Regression_and_Extrapolation": ["FAS2-BIV-LO001", "FAS2-BIV-LO002", "FAS2-BIV-LO003", "FAS2-BIV-LO004", "FAS2-BIV-LO005"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/14_Group_Theory/01_Group_Axioms_Subgroups_and_Isomorphism": ["FAS2-GROUP-LO001", "FAS2-GROUP-LO002", "FAS2-GROUP-LO003", "FAS2-GROUP-LO004", "FAS2-GROUP-LO005", "FAS2-GROUP-LO006", "FAS2-GROUP-LO007", "FAS2-GROUP-LO008", "FAS2-GROUP-LO009"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/15_Graph_Theory/01_Graphs_Trees_and_Traversability": ["FAS2-GRAPH-LO001", "FAS2-GRAPH-LO002", "FAS2-GRAPH-LO003", "FAS2-GRAPH-LO004", "FAS2-GRAPH-LO005"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/16_Algorithms_on_Graphs/01_Critical_Paths_and_Shortest_Paths": ["FAS2-ALGGRAPH-LO001", "FAS2-ALGGRAPH-LO002", "FAS2-ALGGRAPH-LO003", "FAS2-ALGGRAPH-LO004", "FAS2-ALGGRAPH-LO005"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/17_Recurrence_Relationships/01_Recurrence_Models_and_Solutions": ["FAS2-REC-LO001", "FAS2-REC-LO002"],
    "Further_Mathematics/AS_Level/FAS2_Applied_Mathematics/18_Boolean_Algebra/01_Truth_Tables_and_Equivalence": ["FAS2-BOOL-LO001"],

    # --- FA21 PURE FURTHER MATHEMATICS ---
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/01_Proof/01_Mathematical_Induction": ["FA21-PROOF-LO001"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/02_Further_Algebra_and_Functions/01_Partial_Fractions_and_Summation_of_Series": ["FA21-FAF-LO001", "FA21-FAF-LO002", "FA21-FAF-LO003"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/02_Further_Algebra_and_Functions/02_Maclaurin_Series_and_Small_Angles": ["FA21-FAF-LO004", "FA21-FAF-LO005", "FA21-FAF-LO006", "FA21-FAF-LO007"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/03_Complex_Numbers/01_De_Moivres_Theorem_and_Exponential_Form": ["FA21-CN-LO001", "FA21-CN-LO002"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/03_Complex_Numbers/02_Nth_Roots_and_Roots_of_Unity": ["FA21-CN-LO003", "FA21-CN-LO004"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/04_Further_Calculus/01_Improper_Integrals_and_Inverse_Trig": ["FA21-FCALC-LO001", "FA21-FCALC-LO002", "FA21-FCALC-LO003", "FA21-FCALC-LO004"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/04_Further_Calculus/02_Reduction_Formulae_and_Integration_by_Parts": ["FA21-FCALC-LO005", "FA21-FCALC-LO006"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/05_Polar_Coordinates/01_Polar_Coordinates_Curves_and_Area": ["FA21-POLAR-LO001", "FA21-POLAR-LO002", "FA21-POLAR-LO003"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/06_Hyperbolic_Functions/01_Definitions_Graphs_and_Calculus": ["FA21-HYP-LO001", "FA21-HYP-LO002", "FA21-HYP-LO003"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/06_Hyperbolic_Functions/02_Inverse_Hyperbolic_Functions": ["FA21-HYP-LO004", "FA21-HYP-LO005"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/07_Differential_Equations/01_First_Order_and_Integrating_Factors": ["FA21-DE-LO001", "FA21-DE-LO002", "FA21-DE-LO003"],
    "Further_Mathematics/A2_Level/FA21_Pure_Mathematics/07_Differential_Equations/02_Second_Order_Differential_Equations": ["FA21-DE-LO004", "FA21-DE-LO005", "FA21-DE-LO006"],

    # --- FA22 APPLIED FURTHER MATHEMATICS ---
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/01_Simple_Harmonic_Motion/01_SHM_and_Oscillations": ["FA22-SHM-LO001", "FA22-SHM-LO002", "FA22-SHM-LO003", "FA22-SHM-LO004"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/02_Damped_Oscillations/01_Modelling_Damped_Oscillations": ["FA22-DAMP-LO001"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/03_Centre_of_Mass/01_Centre_of_Mass_and_Suspension": ["FA22-COM-LO001", "FA22-COM-LO002", "FA22-COM-LO003", "FA22-COM-LO004", "FA22-COM-LO005"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/04_Frameworks/01_Light_Pin_Jointed_Frameworks": ["FA22-FRAM-LO001"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/05_Further_Circular_Motion_Banked/01_Banked_Corners_Sliding_Overturning": ["FA22-FCM-LO001"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/06_Further_Kinematics/01_Kinematics_3D_and_Variable_Acceleration": ["FA22-FKIN-LO001", "FA22-FKIN-LO002"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/07_Further_Centre_of_Mass/01_Calculus_and_Toppling": ["FA22-FCOM-LO001", "FA22-FCOM-LO002", "FA22-FCOM-LO003", "FA22-FCOM-LO004"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/08_Force_Systems_in_Two_Dimensions/01_Resultants_and_Equivalent_Systems": ["FA22-FSYS-LO001", "FA22-FSYS-LO002"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/09_Restitution/01_Elastic_Collisions_and_Restitution": ["FA22-REST-LO001", "FA22-REST-LO002"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/10_Linear_Combinations/01_Expectation_Variance_and_Normal_Combinations": ["FA22-LINCOMB-LO001", "FA22-LINCOMB-LO002", "FA22-LINCOMB-LO003"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/11_Sampling_and_Estimation/01_Central_Limit_Theorem_and_Confidence_Intervals": ["FA22-EST-LO001", "FA22-EST-LO002", "FA22-EST-LO003", "FA22-EST-LO004"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/12_The_T_Distribution/01_T_Tests_and_Confidence_Intervals": ["FA22-TDIST-LO001", "FA22-TDIST-LO002", "FA22-TDIST-LO003"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/13_Chi_Squared_Tests/01_Goodness_of_Fit_and_Contingency_Tables": ["FA22-CHI2-LO001", "FA22-CHI2-LO002", "FA22-CHI2-LO003"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/14_Counting/01_Inclusion_Exclusion_and_Rook_Polynomials": ["FA22-COUNT-LO001", "FA22-COUNT-LO002"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/15_Graph_Theory_Advanced/01_Matchings_Flows_and_Colourings": ["FA22-GRAPH-LO001", "FA22-GRAPH-LO002", "FA22-GRAPH-LO003", "FA22-GRAPH-LO004"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/16_Algorithms_on_Graphs_Advanced/01_PERT_Simplex_and_Nearest_Neighbour": ["FA22-ALGGRAPH-LO001", "FA22-ALGGRAPH-LO002", "FA22-ALGGRAPH-LO003"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/17_Generating_Functions/01_Generating_Functions_and_Combinatorics": ["FA22-GENFUNC-LO001", "FA22-GENFUNC-LO002", "FA22-GENFUNC-LO003"],
    "Further_Mathematics/A2_Level/FA22_Applied_Mathematics/18_Group_Theory_Advanced/01_Symmetry_Groups_and_Polyas_Theorem": ["FA22-GROUP-LO001", "FA22-GROUP-LO002", "FA22-GROUP-LO003", "FA22-GROUP-LO004", "FA22-GROUP-LO005"]
}

# --- 4. EXECUTION ---
def generate_outcome_files():
    print("Loading Official CCEA Specifications from Source...")
    master_data = {}
    master_data.update(parse_spec_file(MATHS_SPEC_PATH))
    master_data.update(parse_spec_file(FMATHS_SPEC_PATH))
    
    if not master_data:
        print("Failed to load specification data. Aborting.")
        return

    print(f"Successfully loaded {len(master_data)} Learning Outcomes.")
    print("Distributing Learning Outcomes into CCEA_Portal sub-topics...\n")
    
    for relative_path, lo_ids in FOLDER_MAPPING.items():
        folder_path = TARGET_ROOT / relative_path
        
        if folder_path.exists():
            file_path = folder_path / "Learning_Outcomes.md"
            
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(f"# Learning Outcomes & Boundaries\n\n")
                f.write(f"**Target Folder:** `{relative_path.split('/')[-1]}`\n\n")
                f.write("This document defines the EXACT CCEA specification boundaries for this module. During content extraction, you MUST NOT include legacy content that falls outside these parameters.\n\n")
                f.write("---\n\n")
                
                for lo_id in lo_ids:
                    data = master_data.get(lo_id)
                    if data:
                        f.write(f"## {lo_id}\n")
                        f.write(f"**Official Specification Wording:**\n> {data['specification']}\n\n")
                        f.write(f"**Elaboration Guidance:**\n> {data['elaboration']}\n\n")
                        f.write(f"**Student-Friendly Meaning:**\n> {data['student_meaning']}\n\n")
                        f.write(f"**Required Depth / Boundaries:**\n> {data['boundaries']}\n\n")
                        f.write("---\n\n")
                    else:
                        f.write(f"## {lo_id}\n*Data not found in specification map.*\n\n")
            
            print(f"Populated: {relative_path.split('/')[-1]}/Learning_Outcomes.md")
        else:
            print(f"Skipped (Folder not found): {relative_path}")

if __name__ == "__main__":
    generate_outcome_files()
    print("\nSUCCESS: All Learning Outcomes distributed globally across Mathematics and Further Mathematics!")