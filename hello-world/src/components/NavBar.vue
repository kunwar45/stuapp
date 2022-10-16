<template>
<CNavbar expand="lg" color-scheme="light" class="bg-light">
        <CContainer fluid>
          <CNavbarBrand href="#">Navbar</CNavbarBrand>
          <CNavbarToggler @click = "visible = !visible"/>
          <CCollapse class="navbar-collapse" :visible= "visible">
            <CNavbarNav>
              <CNavItem>
                <CNavLink href="#" active>
                  Home
                </CNavLink>
              </CNavItem>
              <CNavItem>
                <CNavLink href="#">Link</CNavLink>
              </CNavItem>
              <CDropdown variant="nav-item" :popper="false">
                <CDropdownToggle color="secondary">Dropdown button</CDropdownToggle>
                <CDropdownMenu>
                  <CDropdownItem href="#">Action</CDropdownItem>
                  <CDropdownItem href="#">Another action</CDropdownItem>
                  <CDropdownDivider />
                  <CDropdownItem href="#">Something else here</CDropdownItem>
                </CDropdownMenu>
              </CDropdown>
              <CNavItem>
                <CNavLink href="#" disabled>
                  Disabled
                </CNavLink>
              </CNavItem>
            </CNavbarNav>
            <CForm class="d-flex">
              <CFormInput type="search" class="me-2" placeholder="Search"/>
              <CButton type="submit" color="success" variant="outline">Search</CButton>
            </CForm>
          </CCollapse>
        </CContainer>
      </CNavbar>
</template>

<script>
// import { CAlert } from '@coreui/vue';
import 'bootstrap/dist/css/bootstrap.min.css'
export default {
  name: 'NavBar',
}
</script>