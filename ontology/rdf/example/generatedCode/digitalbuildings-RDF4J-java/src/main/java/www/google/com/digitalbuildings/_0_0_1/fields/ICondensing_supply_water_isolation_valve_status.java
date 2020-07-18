package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.ICondensing;
import www.google.com.digitalbuildings._0_0_1.subfields.ISupply;
import www.google.com.digitalbuildings._0_0_1.subfields.IIsolation;
import www.google.com.digitalbuildings._0_0_1.subfields.IValve;

public interface ICondensing_supply_water_isolation_valve_status extends IField{

	public IRI iri();

    public void addComposedOfCondensing (ICondensing parameter);

	public Set<ICondensing> getComposedOfCondensing();

    public void addComposedOfIsolation (IIsolation parameter);

	public Set<IIsolation> getComposedOfIsolation();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

    public void addComposedOfSupply (ISupply parameter);

	public Set<ISupply> getComposedOfSupply();

    public void addComposedOfValve (IValve parameter);

	public Set<IValve> getComposedOfValve();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}