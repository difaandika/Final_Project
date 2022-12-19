describe('Final Project', () => {
  it('view my trackers',() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/')
    cy.get("input[placeholder='Username']").type('Admin')
    cy.get("input[placeholder='Password']").type('admin123')
    cy.get("button[type='submit']").click()
    cy.get(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module").should('contain', 'Dashboard')
    cy.get("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > a:nth-child(1)").click()
    cy.get("header[class='oxd-topbar'] li:nth-child(3) a:nth-child(1)").click()
    cy.get("button[name='view']").click()
    cy.get(".oxd-text.oxd-text--h5.orangehrm-employee-tracker-header-title").should('contain', 'Tracker for paul')
  })
})