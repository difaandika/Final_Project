describe('Login', () => {
  it('Success Login',() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/')
    cy.get("input[placeholder='Username']").type('Admin')
    cy.get("input[placeholder='Password']").type('admin123')
    cy.get("button[type='submit']").click()
    cy.get(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module").should('contain', 'Dashboard')
  })

  it('Failed Login with invalid password',() => {
    cy.visit('/')
    cy.get("input[placeholder='Username']").type('Admin')
    cy.get("input[placeholder='Password']").type('asdfg123')
    cy.get("button[type='submit']").click()
    cy.get(".oxd-text.oxd-text--p.oxd-alert-content-text").should('contain', 'Invalid credentials')
  })

  it('Failed Login with invalid username',() => {
    cy.visit('/')
    cy.get("input[placeholder='Username']").type('dodo123')
    cy.get("input[placeholder='Password']").type('admin123')
    cy.get("button[type='submit']").click()
    cy.get(".oxd-text.oxd-text--p.oxd-alert-content-text").should('contain', 'Invalid credentials')
  })

  it('Failed Login with blank field',() => {
    cy.visit('/')
    cy.get("button[type='submit']").click()
    cy.get("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > form:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(3)").should('contain', 'Required')
        cy.get("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > form:nth-child(2) > div:nth-child(3) > div:nth-child(1) > span:nth-child(3)").should('contain', 'Required')
  })
})
