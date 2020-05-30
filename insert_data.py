#import mongoose
import numpy as np
# connect to database
# for each row create a json document
# insert document 

tnames = [
  "Assertiveness",
  "Captiousness",
  "Blunt",
  "Social Confidence",
  "Forgiveness",
  "Stubbornness",
  "Narcissism",
  "Deviousness",
  "Consideration",
  "Empathy",
  "Introversion",
  "Social Dominance",
  "People vs. Things",
  "Disciplined Isolation",
  "Autonomy",
  "Affable",
  "Sociability",
  "Social Dependence",
  "Independent Minded",
  "Aggression",
  "Sensation Seeking",
  "Stress Resilience",
  "Antagonism",
  "Vigilance",
  "Optimism",
  "Surgency",
  "Vigor",
  "Frivolous",
  "Dysthymia",
  "Emotional Reactivity",
  "Negativity",
  "Callousness",
  "Psychopathy",
  "Conflicted Relationships",
  "Nervous Anxiety",
  "Inferiority",
  "Planfulness",
  "Practical vs. Imaginative",
  "Impulse Control",
  "Caution",
  "Orderliness",
  "Detail Conscious",
  "Discipline",
  "Spontaneity",
  "Competence",
  "Unconventionality",
  "Traditionalism",
  "Intolerance",
  "Liberalism",
  "Punitiveness",
  "Simplicity",
  "Dishonest-Opportunism",
  "Novelty Seeking",
  "Resilience",
  "Endurance",
  "Achievement Striving",
  "Sensitivity",
  "Tolerance for Ambiguity",
  "Prejudice",
  "Abstractness",
  "Curiosity",
  "Aesthetic Interests",
  "Cognitive Interests",
  "Creativity",
  "Absorption",
  "Fantasy",
  "Perserverance",
  "Anxiety",
  "Worry",
  "Depression",
  "Rumination",
  "Anger",
  "Embarrassment"
]

thomas_booth_11_factor_cf=[
  0.648, 0.007, 0.082, -0.107, 0.014, 0.006, -0.037, 0.043, -0.087, 0.031, -0.079,
  0.636, -0.187, -0.064, -0.041, -0.102, 0.015, -0.055, -0.014, 0.199, -0.077, 0.208,
  -0.413, 0.019, -0.036, 0.180, -0.117, 0.052, -0.032, 0.054, -0.036, -0.036, 0.023,
  -0.367, 0.092, -0.360, -0.045, 0.067, 0.042, 0.061, 0.020, 0.194, -0.323, 0.294,
  -0.357, 0.205, 0.183, 0.068, 0.049, 0.065, -0.095, -0.021, -0.205, 0.001, -0.051,
  0.338, -0.291, 0.197, -0.135, 0.055, 0.064, -0.016, -0.183, 0.238, 0.117, 0.153,
  0.146, -0.667, 0.083, 0.001, 0.091, 0.030, 0.038, -0.041, -0.038, 0.216, 0.030,
  0.000, -0.591, 0.179, -0.204, 0.144, -0.091, 0.071, 0.038, -0.051, -0.037, 0.055,
  -0.071, -0.453, 0.153, 0.042, 0.225, -0.076, 0.124, -0.180, 0.022, 0.120, -0.024,
  -0.026, 0.369, 0.277, -0.038, 0.315, -0.032, -0.019, -0.102, 0.203, 0.206, 0.340,
  -0.063, -0.107, 0.706, 0.046, 0.165, 0.045,  0.032, -0.003, 0.020, -0.094, 0.129,
  -0.304, 0.178, -0.425, 0.152, 0.058, -0.013, -0.120, 0.104, 0.310, -0.199, 0.120,
  0.149, 0.105, 0.558, 0.077, 0.063, -0.026, -0.071, -0.020, 0.109, -0.036, -0.014,
  0.046, 0.115, 0.565, -0.020, -0.056, 0.043, -0.088, 0.161, -0.106, -0.139, -0.014, 
  0.054, -0.027, -0.540, -0.089, -0.049, -0.013, -0.056, -0.074, -0.155, 0.090, -0.156,
  0.002, 0.264, 0.515, 0.018, 0.417, -0.005, -0.060, -0.162, 0.061, 0.068, -0.060,
  0.289, 0.062, 0.510, 0.030, 0.248, -0.015, -0.128, -0.092, -0.046, 0.078, -0.189,
  -0.033, -0.051, 0.405, -0.029, 0.175, 0.072, 0.072, -0.029, 0.289, -0.030, 0.297,
  0.130, 0.213, -0.396, -0.049, 0.137, -0.043, -0.130, 0.082, -0.042, -0.015, -0.342,
  -0.133, 0.096, 0.013, 0.670, 0.053, -0.038, -0.017, -0.028, -0.034, 0.059, 0.017,
  -0.021, 0.158, 0.036, -0.559, 0.136, -0.021, -0.037, 0.061, -0.329, -0.055, -0.082,
  0.072, -0.026, 0.000, -.537, 0.089, -0.023, 0.071, 0.009, 0.164, -0.102, 0.150,
  -0.139, 0.126, 0.040, 0.522, 0.096, -0.063, -0.151, -0.077, -0.205, 0.046, -0.060,
  -0.002, -0.123, 0.003, 0.517, 0.144, 0.165, -0.107, 0.155, 0.033, -0.060, -0.151,
  0.070, 0.125, 0.014, -0.265, -0.623, -0.096, -0.081, 0.001, 0.135, -0.064, 0.221,
  0.053, 0.182, 0.117, 0.070, 0.577, 0.016, 0.001, 0.076, 0.052, -0.016, -0.085,
  0.281, -0.010, 0.134, 0.058, 0.492, -0.009, 0.079, 0.083, -0.384, -0.085, 0.074,
  -0.113, -0.123, 0.059, -0.203, 0.490, 0.023, -0.096, 0.086, 0.091, -0.012, 0.111,
  -0.233, -0.200, -0.171, -0.033, -0.352, -0.045, -0.043, -0.119, 0.127, -0.034, 0.120,
  0.012, -0.029, -0.034, -0.004, 0.067, 0.820, 0.047, -0.009, -0.067, -0.039, -0.142,
  0.046, -0.006, 0.008, 0.136, -0.012, 0.782, 0.047, -0.009, -0.067, -0.039, -0.058,
  -0.096, 0.187, 0.033, 0.051, 0.038, 0.726, -0.023, 0.061, -0.034, 0.023, 0.210,
  -0.055, 0.143, 0.093, 0.166, -0.127, 0.692, -0.051, 0.058, 0.044, 0.064, 0.059,
  -0.064, -0.056, 0.009, 0.066, 0.010, 0.655, 0.074, -0.177, 0.065, 0.023, -0.113,
  0.129, -0.090, 0.015, -0.140, 0.061, 0.617, -0.036, 0.100, -0.171, 0.072, -0.070,
  -0.257, -0.051, -0.016, 0.027, -0.085, -0.600, 0.033, -0.072, -0.054, 0.013, 0.273,
  0.050, -0.119, -0.010, 0.067, 0.089, -0.012, 0.643, -0.036, 0.002, 0.040, 0.017,
  0.043, 0.016, -0.086, 0.041, 0.061, -0.039, -0.571, 0.095, -0.076, 0.300, 0.093,
  -0.114, 0.052, -0.025, 0.089, -0.083, 0.047, 0.559, -0.146, -0.044, 0.256, -0.159,
  0.066, -0.018, -0.083, -0.045, -0.006, -0.040, 0.002, 0.208, -0.124, 0.634, -0.053,
  0.156, 0.082, 0.002, 0.087, 0.076, -0.002, 0.513, -0.077, -0.170, -0.198, 0.154,
  0.039, 0.039, -0.079, -0.043, -0.041, -0.036, 0.477, -0.09, -0.012, 0.229, 0.128,
  0.291, 0.234, -0.068, 0.108, 0.054, 0.017, 0.471, 0.042, -0.285, -0.210, -0.032,
  -0.077, 0.032, 0.014, 0.258, -0.413, 0.041, 0.430, 0.088, 0.040, 0.084, -0.174,
  0.350, 0.228, -0.103, 0.056, 0.151, -0.059, 0.411, 0.062, -0.113, 0.006, -0.250,
  0.172, 0.343, -0.110, 0.064, 0.013, 0.093, 0.355, -0.323, -0.101, 0.073,0.021,
  0.033, -0.124, -0.316, -0.010, 0.099, -0.121, -0.323, 0.031, -0.154, 0.286, 0.251,
  0.018, -0.019, -0.027, -0.085, 0.007, 0.025, -0.165, 0.762, -0.006, 0.072, 0.017,
  -0.016, -0.051, -0.004, -0.070, 0.065, -0.094, 0.012, 0.714, -0.033, -0.127, 0.064,
  -0.022, -0.116, -0.076, -0.124, 0.167, 0.025, 0.120, 0.658, 0.057, 0.087, 0.006,
  0.006, 0.080, 0.025, 0.081, 0.022, 0.066, -0.030, 0.541, 0.069, 0.148, 0.000,
  -0.163, -0.054, -0.116, -0.093, 0.214, 0.033, 0.107, -0.457, 0.084, -0.194, -0.123,
  0.012, -0.310, -0.015, 0.220, 0.032, -0.335, 0.061, 0.368, -0.019, -0.115, -0.014,
  0.078, 0.083, -0.037, -0.041, 0.162, 0.021, -0.106, 0.346, -0.208, 0.307, 0.057,
  0.038, 0.087, 0.130, 0.287, -0.101, -0.035, 0.115, 0.075, 0.564, 0.003, 0.153,
  -0.021, 0.045, 0.123, 0.054, -0.110, 0.016, -0.182, 0.128, 0.491, -0.268, -0.189,
  0.188, -0.064, -0.009, 0.016, 0.153, -0.021, 0.229, -0.094, 0.477, 0.147, 0.319,
  -0.019, -0.329, -0.045, -0.132, -0.127, -0.065, -0.017, -0.227, -0.405, -0.219, -0.111,
  -0.093, -0.089, -0.060, 0.202, -0.021, -0.058, 0.243, -0.277, 0.398, -0.101, 0.025,
  0.080, -0.252, -0.231, 0.084, -0.046, -0.049, 0.106, -0.289, 0.337, -0.095, -0.014,
  0.066, -0.018, -0.083, -0.045, -0.006, -0.040, 0.002, 0.208, -0.214, 0.634, -0.053,
  -0.050, 0.010, -0.042, -0.031, 0.011, -0.015, -0.010, -0.246, 0.005, -0.614, 0.041,
  -0.072, 0.093, -0.068, 0.033, 0.195, 0.026, -0.005, 0.256, 0.085, 0.519, 0.008,
  0.213, 0.071,0.022, -0.002, -0.144, 0.063, 0.041, 0.118, -0.309, 0.469, 0.002,
  0.121, 0.017, 0.022, -0.002, -0.144, 0.063, 0.041, 0.118, -0.309, 0.459, 0.040,
  0.186, -0.082, -.032, 0.332, -0.361, 0.071, -0.008, 0.040, -0.055, -0.441, -0.180,
  -0.009, 0.018, -0.071, -0.108, 0.114, -0.004, -0.236, -0.253, 0.127, 0.127, 0.374, 0.001
  -0.148, -0.068, 0.170, 0.057, 0.014, -0.262, -0.186, 0.137, 0.321, -0.356, -0.128
  -0.036, -0.021, 0.030, -0.214, -0.050, -0.144, -0.091, 0.111, 0.040, 0.102, 0.000,0.663,
  0.021, -0.001, 0.128, -0.017, -0.144, -0.091, 0.111, 0.040, 0.102, 0.000, 0.663,
  -0.051, -0.044, -0.010, -0.018, -0.199, -0.115, -0.237, 0.018, -0.021, 0.048, 0.658,
  0.189, 0.026, -0.016, -0.024, 0.054, 0.112, -0.001, 0.088, 0.038, -0.077, -0.589,
  0.319, -0.161, -0.059, -0.213, -0.021, -0.069, -0.125, 0.005, 0.130, -0.076,0.474,
  -0.062, 0.062, -0.076, 0.065, -0.098, -0.047, 0.087, 0.009, 0.242, -0.014, 0.449 ]

translation_matrix_five_to_thomas_booth=[
  0,0,1,0,0,
  0,0,0,1,0,
  0,0,0,1,0,
  0,0,0,0,1,
  0,0,1,0,0,
  0,0,0,0,1,
  0,1,0,0,0,
  1,0,0,0,0,
  0,1,0,0,0,
  1,0,0,0,0,
  0,0,0,0,1
]

A = np.array( thomas_booth_11_factor_cf ).reshape(74, 11)
B = np.array( translation_matrix_five_to_thomas_booth ).reshape(11,5)

traits_matrix = np.transpose(np.dot(A,B))

f = open( 'bigfive.csv', 'r')

# assume traits names

def create_traits_dict( v, q ):
    d['o'] = v[0]
    d['c'] = v[1]
    d['e'] = v[2]
    d['a'] = v[3]
    d['n'] = v[4]
    for k in range(len(tnames)):
        d[tnames[k]]=q[k]
    return d

def transform_to_traits_dict( big_five_vec ):
    q = np.dot(big_five_vec,traits_matrix)
    d = create_traits_dict( big_five_vec, q )
    return d

for line in f:
    d = dict()
    z = line.split(',')
    v = np.array(z).astype(np.float)
    d = transform_to_traits_dict( v )
    print d
    #db.profiles.insertOne( d )



