describe('Final Project', () => {
  it('Search employee by name ',() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/')
    cy.get("input[placeholder='Username']").type('Admin')
    cy.get("input[placeholder='Password']").type('admin123')
    cy.get("button[type='submit']").click()
    cy.get(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module").should('contain', 'Dashboard')
    cy.get("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
    cy.get("input[placeholder='Type for hints...']").type('Charlie Carter')
    cy.get("button[type='submit'].oxd-button ").click()
    cy.get(".oxd-text.oxd-text--h6.orangehrm-main-title").should('contain', 'Timesheet for Charlie Carter')
  })
  
  it('View one of Timesheets list',() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/')
    cy.get("input[placeholder='Username']").type('Admin')
    cy.get("input[placeholder='Password']").type('admin123')
    cy.get("button[type='submit']").click()
    cy.get(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module").should('contain', 'Dashboard')
    cy.get("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
    cy.get("div[role='table'] div:nth-child(1) div:nth-child(1) div:nth-child(3) div:nth-child(1) button:nth-child(1)").click()
  })
})