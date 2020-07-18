package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IFlowrate;
import www.google.com.digitalbuildings._0_0_1.subfields.ICooling;
import www.google.com.digitalbuildings._0_0_1.subfields.ICapacity;
import www.google.com.digitalbuildings._0_0_1.subfields.ISupply;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;

public interface ISupply_air_cooling_flowrate_capacity extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfCapacity (ICapacity parameter);

	public Set<ICapacity> getComposedOfCapacity();

    public void addComposedOfCooling (ICooling parameter);

	public Set<ICooling> getComposedOfCooling();

    public void addComposedOfFlowrate (IFlowrate parameter);

	public Set<IFlowrate> getComposedOfFlowrate();

    public void addComposedOfSupply (ISupply parameter);

	public Set<ISupply> getComposedOfSupply();

}