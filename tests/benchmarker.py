import time
from proteinseqRetriever.py import main

def run_single_query(query):
    """
    Run a single UniProt query test and return the result.
    Args:
        query (str): UniProt ID or protein name.
    Returns:
        dict: Result of the test, including the query, sequence length, and time taken.
    Raises:
        ValueError: If the sequence is invalid or not found.
    """
    start_time = time.time()
    # Retrieve amino acid sequence
    aa_sequence = main(query)  # Call the main function from your script
    elapsed_time = time.time() - start_time
    # Raise an error if the sequence is invalid
    if not aa_sequence or not aa_sequence.isalpha():
        raise ValueError(f"No valid sequence found for query: {query}") 
    # Check the sequence with the checkers
    checkers = [
        ValidAASequenceChecker(),
        EmptyAASequenceChecker(),
        SpecialCharacterAASequenceChecker(),
        LowercaseAASequenceChecker(),
        UncommonCharacterAASequenceChecker()
    ]
    # Validate using the checkers
    validation_results = {}
    for checker in checkers:
        validation_results[checker.__class__.__name__] = checker.run(aa_sequence)
    return {
        "Query": query,
        "Sequence Length": len(aa_sequence),
        "Time (s)": round(elapsed_time, 4),
        "Validation Results": validation_results
    }

def benchmark_queries(queries):
    """
    Run a series of UniProt queries and collect benchmark results.
    Args:
        queries (list): List of UniProt IDs or protein names to query.
    Returns:
        list: Results for all queries, including sequence lengths and times.  
    Raises:
        ValueError: If any query result is invalid.
    """
    results = []
    for query in queries:
        result = run_single_query(query)
        results.append(result)
    return results

PROTEIN_QUERIES = [
    "P69905", "P68871", "TP53", "P04637", "P00734", "thrombin", "P00915", "carbonic anhydrase",
    "P19835", "trypsin", "P08240", "lysozyme", "P68431", "histone H3", "P62805", "histone H4",
    "P02768", "albumin", "P01834", "immunoglobulin", "P01375", "insulin", "Q96PD5", "myosin",
    "P01111", "Ras", "P20060", "collagen", "Q9Y6S2", "actin", "P0A7T0", "ribosomal protein",
    "Q9Y5I9", "GTPase", "P04049", "fibrinogen", "P20840", "tubulin", "P02647", "glucagon",
    "Q9NZI2", "E-cadherin", "Q6P0D0", "cytochrome c", "P0DTC2", "RNA polymerase", "Q9H9P2",
    "parkin", "P02545", "growth hormone", "P00010", "alpha-1 antitrypsin", "P08908", "fibronectin",
    "Q9UKB2", "calmodulin", "P21802", "myoglobin", "P06493", "matrix metalloproteinase",
    "Q9C0H0", "hemoglobin subunit", "P11021", "actin alpha cardiac", "P06104", "histone deacetylase",
    "P68852", "catalase", "P02358", "angiotensin", "P06213", "serotonin transporter", "P29274",
    "apolipoprotein", "Q8N5X9", "heat shock protein", "P37268", "lymphocyte activation", "Q9UM73",
    "ATP synthase", "P07711", "protein kinase", "Q96S51", "serine protease", "P00310", "plasminogen",
    "Q16539", "tumor suppressor", "P01012", "vitamin D binding protein", "P26822", "interferon",
    "Q03135", "glutamate receptor", "Q9BZB5", "glutathione S-transferase", "Q9UH85", "zinc finger protein",
    "P62979", "peptidase", "Q9Y257", "tyrosine kinase", "Q16539", "Tumor necrosis factor", "P12931",
    "beta-actin", "P04264", "Ephrin receptor", "Q13159", "fibroblast growth factor", "P07019",
    "neurotrophin", "P07805", "peroxisome proliferator", "P28061", "ATP-binding cassette",
    "P01012", "vitamin D binding protein", "P48729", "calbindin", "P40101", "integrin", "P25630",
    "osteopontin", "P08069", "glycogen synthase", "P04217", "annexin", "P14618", "vascular endothelial growth factor",
    "P10415", "interleukin", "P19387", "interleukin receptor", "P35557", "caspase", "P04233", "interferon-gamma",
    "P05362", "chemokine", "Q92964", "insulin receptor", "Q9NYY7", "cytokine receptor", "P00559", "lactate dehydrogenase",
    "P09467", "osteocalcin", "bhuR", "lacZ", "gyrA", "recA", "rpoB", "dnaK", "dnaJ", "fhlA", "fabI", "araC",
    "metA", "pheA", "tnaA", "hisA", "pyrE", "purA", "trpA", "ompA", "yfiR", "tolC", "glnA", "acpP", "rpsL",
    "greA", "thrA", "ptsI", "pepA", "ppdA", "cysK", "argA", "tpiA", "rpsB", "kdpA", "nmpC", "marA",
    "gatA", "nagA", "ecpA", "fliC", "flhD", "cheA", "cheW", "cheY", "sipB", "sipA", "invA", "fimA",
    "ycdH", "wrbA", "hemA", "glpK", "malT", "mglB", "glk", "pdhA", "pfkA", "hns", "luxS", "crp", "lacI",
    "acpP", "clpX", "hibA", "tufA", "phyA", "rfaH", "ompC", "ompF", "tsf", "flhC", "fliG", "degP", "hipA",
    "cipA", "kdpB", "sipC", "uvrA", "uvrB", "mutS", "mutL", "mutH", "xseA", "xseB", "xseC"
]

if __name__ == "__main__":
    benchmark_results = benchmark_queries(PROTEIN_QUERIES)
