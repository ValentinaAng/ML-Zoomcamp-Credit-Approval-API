from typing import Literal

from pydantic import BaseModel, Field


class InputData(BaseModel):
    checking_status: Literal["0_checking", "from_0_to_200", "more_than_200"] = Field(
        ...,
        description="Status of existing checking account",
    )

    duration: int = Field(..., description="Duration in months")

    credit_history: Literal[
        "Critical_acct_other_credits_existing",
        "Existing_credits_paid_till_now",
        "Delay_in_past",
        "No_credits_taken_or_all_paid",
        "All_credits_paid_duly",
        "other",
    ] = Field(
        ...,
        description="Credit history (credits taken, paid back duly, delays, critical accounts)",
    )

    purpose: Literal[
        "radio/television",
        "education",
        "furniture/equipment",
        "new_car",
        "used_car",
        "business",
        "domestic_appliances",
        "repairs",
        "other",
        "retraining",
    ] = Field(..., description="Purpose of the credit")

    credit_amount: float = Field(..., description="Amount of the credit")

    savings_status: Literal[
        "Unknown_or_no_savings_acct",
        "<100DM",
        "500_to_1000DM",
        ">1000DM",
        "100_to_500DM",
    ] = Field(..., description="Status of savings account in Deutsche Mark")

    employment: Literal[">7yrs", "1_to_4yrs", "4_to_7yrs", "unemployed", "<1yr"] = Field(
        ...,
        description="Status of employment, in years",
    )

    installment_commitment: float = Field(
        ...,
        description="Installment rate in percentage of disposable income",
    )

    personal_status: Literal[
        "male_single",
        "female_divorced/separated/married",
        "male_divorced/separated",
        "male_married/widowed",
    ] = Field(..., description="Sex and personal status")

    other_parties: Literal["guarantor", "co-applicant", "other"] = Field(
        ...,
        description="Other debtors / guarantors",
    )

    residence_since: int = Field(..., description="Years of residence")

    property_magnitude: Literal[
        "real_estate",
        "building_society_savings_agreement/life_insurance",
        "unknown/no_property",
        "car_or_other_nonsavings",
        "other",
    ] = Field(..., description="Property/real estate")

    age: int = Field(..., description="Age")

    other_payment_plans: Literal["none", "bank", "stores", "other"] = Field(
        ...,
        description="Other installment plans (banks, stores)",
    )

    housing: Literal["own", "for_free", "rent"] = Field(..., description="Housing type")

    existing_credits: int = Field(..., description="Number of existing credits at this bank")

    job: Literal[
        "skilled_employee/official",
        "unskilled_resident",
        "management_self-employed_highly_qualified/officer",
        "unemployed/unskilled_nonresident",
        "other",
    ] = Field(..., description="Employment type")

    num_dependents: int = Field(
        ...,
        description="Number of people being liable to provide maintenance for",
    )

    own_telephone: Literal["yes", "no"] = Field(..., description="Own telephone")
    foreign_worker: Literal["yes", "no"] = Field(..., description="Foreign worker")
