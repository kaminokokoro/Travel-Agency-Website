// import __taxonomies from "./jsons/__taxonomies.json";
import __stayTaxonomies from "./jsons/__stayTaxonomies.json";
import __experiencesTaxonomies from "./jsons/__experiencesTaxonomies.json";
import { TaxonomyType } from "./types";

//

const DEMO_STAY_CATEGORIES: TaxonomyType[] = __stayTaxonomies.map((item) => ({
  ...item,
  taxonomy: "category",
  listingType: "stay",
}));
//
const DEMO_EXPERIENCES_CATEGORIES: TaxonomyType[] = __experiencesTaxonomies.map(
  (item) => ({
    ...item,
    taxonomy: "category",
    listingType: "experiences",
  })
);

export {
  DEMO_STAY_CATEGORIES,
  DEMO_EXPERIENCES_CATEGORIES,
};
