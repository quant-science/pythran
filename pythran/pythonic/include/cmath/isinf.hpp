#ifndef PYTHONIC_INCLUDE_CMATH_ISINF_HPP
#define PYTHONIC_INCLUDE_CMATH_ISINF_HPP

#include "pythonic/include/utils/functor.hpp"
#include "pythonic/include/types/complex.hpp"

#include <cmath>

PYTHONIC_NS_BEGIN

namespace cmath
{
  DEFINE_FUNCTOR_2(isinf, std::isinf);
}
PYTHONIC_NS_END

#endif
