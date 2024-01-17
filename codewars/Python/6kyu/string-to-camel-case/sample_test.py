import codewars_test as test
from solution import to_camel_case


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(to_camel_case(""), "", "An empty string was provided but not returned")
        test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")