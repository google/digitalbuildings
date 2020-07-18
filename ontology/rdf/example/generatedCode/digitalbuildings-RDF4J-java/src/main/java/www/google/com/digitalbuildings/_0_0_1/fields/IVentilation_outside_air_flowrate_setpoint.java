package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IFlowrate;
import www.google.com.digitalbuildings._0_0_1.subfields.ISetpoint;
import www.google.com.digitalbuildings._0_0_1.subfields.IVentilation;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IOutside;

public interface IVentilation_outside_air_flowrate_setpoint extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfFlowrate (IFlowrate parameter);

	public Set<IFlowrate> getComposedOfFlowrate();

    public void addComposedOfOutside (IOutside parameter);

	public Set<IOutside> getComposedOfOutside();

    public void addComposedOfSetpoint (ISetpoint parameter);

	public Set<ISetpoint> getComposedOfSetpoint();

    public void addComposedOfVentilation (IVentilation parameter);

	public Set<IVentilation> getComposedOfVentilation();

}