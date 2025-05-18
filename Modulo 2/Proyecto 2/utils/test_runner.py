import unittest
import io

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('test')

    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)

    output = stream.getvalue()

    test_results = []

    failed_or_errored = {str(t[0]) for t in result.failures + result.errors}

    # Recorremos todas las pruebas del suite
    def extract_test_cases(suite):
        for test in suite:
            if isinstance(test, unittest.TestSuite):
                yield from extract_test_cases(test)
            else:
                yield test

    for case in extract_test_cases(suite):
        name = str(case)
        if name in failed_or_errored:
            continue  # Ya está en failures/errors, se agregan abajo
        test_results.append({
            "name": name,
            "status": "ok"
        })

    for failed_test, traceback in result.failures:
        test_results.append({
            "name": str(failed_test),
            "status": "fail",
            "details": traceback
        })

    for error_test, traceback in result.errors:
        test_results.append({
            "name": str(error_test),
            "status": "error",
            "details": traceback
        })

    return output, result.wasSuccessful(), test_results
