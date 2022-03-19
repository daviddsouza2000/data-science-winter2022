create table if not exists data_mart."FactTable"
(
    "YearKey"               integer,
    "CountryKey"            integer,
    "EducationKey"          integer,
    "QualityOfLifeKey"      integer,
    "HealthKey"             integer,
    "PopulationKey"         integer,
    "QualityOfLife"         integer,
    "DevelopmentIndex"      integer,
    "HumanDevelopmentIndex" integer
);

create table if not exists data_mart."Year"
(
    "YearKey"    integer not null
        constraint month_pk
            primary key,
    "Year"       integer,
    "IsLeapYear" boolean
);

create table if not exists data_mart."Country"
(
    "CountryKey"        integer not null
        constraint country_pk
            primary key,
    "Name"              varchar(56),
    "ALPHA-3"           varchar(3),
    "ALPHA-2"           varchar(2),
    "Region"            varchar(255),
    "Continent"         varchar(85),
    "Currency"          varchar(3),
    "Capital"           varchar(85),
    "TotalPopulation"   integer,
    "Birthrate"         double precision,
    "Size"              integer,
    gdp                 double precision,
    "PopulationDensity" double precision
);

create table if not exists data_mart."Education"
(
    "EducationKey"                              integer not null
        constraint education_pk
            primary key,
    "LiteracyRateFemale"                        double precision,
    "LiteracyRateMale"                          double precision,
    "LiteracyRateTotal"                         double precision,
    "SchoolEnrollmentPrimary"                   double precision,
    "SchoolEnrollmentSecondary"                 double precision,
    "SchoolEnrollmentTertiary"                  double precision,
    "PublicEducationSpending"                   double precision,
    "PISAMeanMathPerformance"                   integer,
    "PISAMeanReadingPerformance"                integer,
    "PISAMeanSciencePerformance"                integer,
    "GenderParityIndexForGrossEnrolmentPrimary" double precision
);

create table if not exists data_mart."Health"
(
    "HealthKey"                     integer not null
        constraint health_pk
            primary key,
    "DomesticHealthExpenditure"     double precision,
    "HospitalBeds"                  integer,
    "HepImmunization"               double precision,
    "DPTImmunization"               double precision,
    "MeaslesImmunization"           double precision,
    "PolioImmunization"             double precision,
    "InfantMortality"               double precision,
    "Stillbirths"                   double precision,
    "NumberOfNurses"                double precision,
    "NumberOfDoctors"               double precision,
    "PrevalenceOfDiabetes"          double precision,
    "PrevalenceOfHIV"               double precision,
    "PrevalenceOfCurrentTobaccoUse" double precision,
    "TotalAlcoholConsumption"       double precision,
    "AdultMortalityMale"            double precision,
    "AdultMortalityFemale"          double precision
);

create table if not exists data_mart."QualityOfLife"
(
    "QualityOfLifeKey"                       integer not null
        constraint qualityoflife_pk
            primary key,
    "AccessToDrinkingWater"                  double precision,
    "AccessToSanitation"                     double precision,
    "AccessToBasicHandwashingFacilities"     double precision,
    "UnemploymentFemale"                     double precision,
    "UnemploymentMale"                       double precision,
    "UnemploymentTotal"                      double precision,
    "PregnantWomanReceivingPrenatalCare"     double precision,
    "AgeDependencyRatio"                     double precision,
    "BirthsAttendedBySkilledHealthcareStaff" double precision,
    "CommunityHealthWorkers"                 double precision,
    "ConsumptionOfIodisedSalt"               double precision
);

create table if not exists data_mart."Population"
(
    "PopulationKey"                 integer not null
        constraint population_pk
            primary key,
    "LifeExpectancyFemale"          double precision,
    "LifeExpectancyMale"            double precision,
    "LifeExpectancyTotal"           double precision,
    "NetMigration"                  double precision,
    "PopulationGrowth"              double precision,
    "LabourForceFemale"             double precision,
    "LabourForceTotal"              double precision,
    "RuralPopulationGrowth"         double precision,
    "UrbanPopulationGrowth"         double precision,
    "RuralPercentOfTotalPopulation" double precision,
    "UrbanPercentOfTotalPopulation" double precision
);

create table if not exists data_mart."Events"
(
    "EventKey"    integer,
    "YearKey"     integer,
    "Name"        text,
    "Description" text,
    "Type"        text
);

create table if not exists data_mart."EventBridge"
(
    "CountryKey" integer,
    "YearKey"    integer,
    "EventKey"   integer
);