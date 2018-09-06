import pytest
from user_manager import UserManager

# Pytest testing file
# A total of 23 tests
# Testing:
#	empty UserManager (1)
#	adding to patients list (3)
#	adding to provider list (3)
#	removing from patient list (3)
#	removing from provider list (3)
#	searching by patient name (4)
#	searching by provider name (4)
#	search by service (2)

# Test User Manager
def test_empty_user_manager():
	um = UserManager()
	assert(len(um.patients) == 0)
	assert(len(um.providers) == 0)

# test adding new to patients

# test adding nothing to patients

# test adding an existing patient to patients


# test adding new to providers

# test adding nothing to proiders

# test adding an existing provider to proiders


# test removing existing from patients

# test removing non-existing from patients

# test removing from empty patients


# test removing existing from providers

# test removing non-existing from providers

# test removing from empty providers


# test search for existing patient by exact name

# test search for existing patient by near exact name

# test search for NON-existing patient by exact name

# test search for NON-existing patient by near exact name


# test search for existing provider by exact name

# test search for existing provider by near exact name

# test search for NON-existing provider by exact name

# test search for NON-existing provider by near exact name


# test search for existing service

# test search for non-existing service 